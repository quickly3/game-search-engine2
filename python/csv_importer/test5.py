import pandas as pd
import numpy as np


def extract_city_name(df):
    """
    Chicago, IL -> Chicago for city_name column
    """
    df['city_name'] = df['city_and_code'].str.split(",").str.get(0)
    return df


def add_country_name(df, country_name=None):
    """
    Chicago -> Chicago-US for city_name column
    """
    col = 'city_name'
    df['city_and_country'] = df[col] + country_name
    return df


df_p = pd.DataFrame({'city_and_code': ['Chicago, IL']})

# add_country_name(extract_city_name(df_p), country_name=', US')


(df_p.pipe(extract_city_name).pipe(add_country_name, country_name="US"))

print(df_p)
