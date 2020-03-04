# crawler https://github.com/ranaroussi/yfinance


# pip3 install yfinance
# pip3 install sqlalchemy
# pip3 install pandas
# pip3 install numpy
# pip3 install requests
# pip3 install pandas_datareader
# pip3 install python-dotenv
# pip3 install pathlib
# pip3 install pymysql


# run
# python3 yf_stock_crawl.py

from pandas_datareader import data as pdr
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from string import Template

import yfinance as yf
import os
import numpy as np
import pandas as pd

from dotenv import load_dotenv
from pathlib import Path
env_path = Path('..')/'.env'
load_dotenv(dotenv_path=env_path)

MY_HOST = os.getenv("DB_HOST")
MY_DATABASE = os.getenv("DB_DATABASE")
MY_USERNAME = os.getenv("DB_USERNAME")
MY_PASSWORD = os.getenv("DB_PASSWORD")

PG_HOST = os.getenv("DB_HOST2")
PG_PORT = os.getenv("DB_PORT2")
PG_DATABASE = os.getenv("DB_DATABASE2")
PG_USERNAME = os.getenv("DB_USERNAME2")
PG_PASSWORD = os.getenv("DB_PASSWORD2")


# MY_DATABASE = 'execsearch'
# MY_USERNAME = 'root'
# MY_PASSWORD = 'root'

# PG_HOST = '35.169.147.220'
# PG_PORT = '5432'
# PG_DATABASE = 'ciq_target'
# PG_USERNAME = 'postgres'
# PG_PASSWORD = 'Titan1qaz2wsx'


def pg_session():
    engine = create_engine("postgresql+psycopg2://"+PG_USERNAME+":"+PG_PASSWORD +
                           "@"+PG_HOST+"/"+PG_DATABASE, encoding='utf-8', echo=False)

    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    return session


def mysql_session():
    engine = create_engine("mysql+pymysql://"+MY_USERNAME+":"+MY_PASSWORD +
                           "@"+MY_HOST+"/"+MY_DATABASE+"?charset=utf8", encoding='utf-8', echo=False)

    session_factory = sessionmaker(bind=engine)
    session = session_factory()
    return session


def init_base_ticker():
    pg_s = pg_session()
    my_s = mysql_session()

    sql = """\
        SELECT c.companyid,re.exchangesymbol,ti.tickersymbol
        FROM ciqcompany as c
        JOIN ciqsecurity as s ON c.companyid = s.companyid
        JOIN ciqtradingitem as ti ON s.securityid = ti.securityid
        JOIN refexchange as re ON re.exchangeid = ti.exchangeid
        WHERE re.exchangeid in (104, 106,173,458)
        AND ti.tradingitemstatusid = 15
        AND ti.primaryflag = 1
        AND s.primaryflag = 1
       """

    try:
        resultproxy = pg_s.execute(
            text(sql)
        )
    except Exception as e:
        print(e)
        results = []
    else:
        results = resultproxy.fetchall()

    for item in results:
        sql_tpl = Template(
            "insert into ciq_exchange_ticker values(0,'${ciqid}','${exchange}','${ticker}','${ticker_adj}',0)")

        if item[2]:
            ticker_adj = item[2].replace(".", "")
            sql = sql_tpl.substitute(
                ciqid=item[0], exchange=item[1], ticker=item[2], ticker_adj=ticker_adj)

            my_s.execute(sql)
            my_s.commit()


def updateState(id, state):

    sql_tpl = Template(
        "update ciq_exchange_ticker set state=${state} where id=${id}")
    sql = sql_tpl.substitute(
        state=state, id=id)

    my_s.execute(sql)
    my_s.commit()


def ticker_count():
    sql = """\
        SELECT count(1)
        FROM ciq_exchange_ticker
        where state = 0
       """
    try:
        resultproxy = my_s.execute(
            text(sql)
        )
    except Exception as e:
        print(e)
        results = []
    else:
        results = resultproxy.fetchall()

    count = results[0][0]

    return count


def test():
    yf.pdr_override()  # <== that's all it takes :-)

    # download dataframe
    resp = pdr.get_data_yahoo(
        "CWENA", start="2000-01-01", end="2019-12-31")
    print(resp)
    if resp.empty == True:
        updateState(1990, 2)
    else:
        insert_stock_price(resp, "CWENA")
        updateState(1990, 1)


def insert_stock_price(df, ticker_adj):

    datas = []

    for index, row in df.iterrows():

        if str(row['Volume']) == 'nan':
            row['Volume'] = 0

        data = [0, ticker_adj, row['Open'], row['High'], row['Low'],
                row['Close'], row['Adj Close'], row['Volume'], index]
        datas.append(data)

    datas_chunk = chunks(datas, 500)

    for chunk_datas in datas_chunk:
        sql = "insert into yf_ticker_price values"
        values_arr = []

        for item in chunk_datas:

            item_str = ('"'+item1+'"' for item1 in map(str, item))
            values_arr.append("("+",".join(item_str)+")")

        chunk_sql = sql+",".join(values_arr)

        my_s.execute(chunk_sql)
        my_s.commit()

    # print(datas)
    # print(datas)

    # val_tpl = Template(
    #     "(0,'${ciqid}','${exchange}','${ticker}','${ticker_adj}',0)")

    # if item[2]:
    #     ticker_adj = item[2].replace(".", "")
    #     sql = sql_tpl.substitute(
    #         ciqid=item[0], exchange=item[1], ticker=item[2], ticker_adj=ticker_adj)


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def crawl_stock_price():

    count = ticker_count()
    current = 0
    sql = """\
        SELECT id,ticker
        FROM ciq_exchange_ticker where state = 0
       """
    try:
        resultproxy = my_s.execute(
            text(sql)
        )
    except Exception as e:
        print(e)
        results = []
    else:
        results = resultproxy.fetchall()

    for item in results:
        ticker = item[1]
        ticker_adj = ticker.replace(".", "")
        current += 1
        print(str(current)+"/"+str(count))
        print("Downloading:"+ticker_adj)

        id = item[0]

        yf.pdr_override()  # <== that's all it takes :-)

        # download dataframe
        resp = pdr.get_data_yahoo(
            ticker_adj, start="2000-01-01", end="2019-12-31")

        if resp.empty == True:
            updateState(id, 2)
        else:
            insert_stock_price(resp, ticker_adj)
            updateState(id, 1)


def quarter_stock_price():
    count = ticker_count()
    current = 0
    sql = """\
        SELECT id,ticker_adj
        FROM ciq_exchange_ticker where state = 1
       """
    try:
        resultproxy = my_s.execute(
            text(sql)
        )
    except Exception as e:
        print(e)
        results = []
    else:
        results = resultproxy.fetchall()

    for item in results:
        current = current + 1
        print(current)
        print(item['ticker_adj'])

        get_quarter_stock_price(item)


def get_quarter_stock_price(ticker_obj):

    lookup = {

        1: 'q1',
        2: 'q1',
        3: 'q1',
        4: 'q2',
        5: 'q2',
        6: 'q2',
        7: 'q3',
        8: 'q3',
        9: 'q3',
        10: 'q4',
        11: 'q4',
        12: 'q4'
    }

    ticker = ticker_obj['ticker_adj']

    sql_tpl = Template("""\
        SELECT close_adj,date
          FROM yf_ticker_price
         WHERE ticker_adj = '${ticker}'
           AND close_adj > 0
      ORDER BY date
       """)

    sql = sql_tpl.substitute(ticker=ticker)

    try:
        resultproxy = my_s.execute(
            text(sql)
        )
    except Exception as e:
        print(e)
        results = []
    else:
        results = resultproxy.fetchall()

    if len(results) > 0:
        # prices = [price[0] for price in results]
        df = pd.DataFrame(data=results)
        df.columns = ["close", "date"]
        df['season'] = df['date'].apply(lambda x: lookup[x.month])
        df['year'] = df['date'].apply(lambda x: x.year)

        df['count'] = 1
        df_agg = df.groupby(['year', 'season'])['close', 'count'].sum()
        df_agg['average'] = df_agg['close'] / df_agg['count']
        df_agg['ticker_adj'] = ticker
        df_agg['id'] = 0

        df2 = df_agg.reset_index()
        list = df2[['id', 'ticker_adj', 'year',
                    'season', 'average']].values.tolist()

        sql = "insert into yf_ticker_quarter_price values"
        values_arr = []

        for record in list:
            item_str = ('"'+item1+'"' for item1 in map(str, record))
            values_arr.append("("+",".join(item_str)+")")

        chunk_sql = sql+",".join(values_arr)

        my_s.execute(chunk_sql)
        my_s.commit()

        # for item2 in df_agg.values.tolist():
        #     print(item2)


my_s = mysql_session()
quarter_stock_price()
# test()
