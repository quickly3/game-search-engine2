# -*- coding: utf-8 -*-
import json
import requests
import re
import random
import urllib
import lxml.html
import bs4
import sys


HEADERS = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'accept-encoding': 'gzip, deflate, sdch',
           'accept-language': 'en-US,en;q=0.8',
           'upgrade-insecure-requests': '1',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
file = open('company_data.json', 'w')
file.write('[')
file.close()
COUNT = 0

def increment():
    global COUNT
    COUNT = COUNT+1

def fetch_request(url):
  try:
      fetch_url = requests.get(url, headers=HEADERS)
  except:
      try:
          fetch_url = requests.get(url, headers=HEADERS)
      except:
          try:
              fetch_url = requests.get(url, headers=HEADERS)
          except:
              fetch_url = ''
  return fetch_url

def parse_company_urls(company_url):

    if company_url:
        if '/company/' in company_url:
            parse_company_data(company_url)
        else:
            parent_url = company_url
            fetch_company_url=fetch_request(company_url)
            if fetch_company_url:
                sel = lxml.html.fromstring(fetch_company_url.content)
                COMPANIES_XPATH = '//div[@class="section last"]/div/ul/li/a/@href'
                companies_urls = sel.xpath(COMPANIES_XPATH)
                if companies_urls:
                    if '/company/' in companies_urls[0]:
                        print('Parsing From Category ', parent_url)
                        print('-------------------------------------------------------------------------------------')
                    for company_url in companies_urls:
                        parse_company_urls(company_url)
            else:
                pass


def parse_company_data(company_data_url):

    if company_data_url:
        fetch_company_data = fetch_request(company_data_url)
        if fetch_company_data.status_code == 200:
            try:
                source = fetch_company_data.content.decode('utf-8')
                sel = lxml.html.fromstring(source)
                # CODE_XPATH = '//code[@id="stream-promo-top-bar-embed-id-content"]'
                # code_text = sel.xpath(CODE_XPATH).re(r'<!--(.*)-->')
                code_text = sel.get_element_by_id(
                    'stream-promo-top-bar-embed-id-content')
                if len(code_text) > 0:
                    code_text = str(code_text[0])
                    code_text = re.findall(r'<!--(.*)-->', str(code_text))
                    code_text = code_text[0].strip() if code_text else '{}'
                    json_data = json.loads(code_text)
                    if json_data.get('squareLogo', ''):
                        company_pic = 'https://media.licdn.com/mpr/mpr/shrink_200_200' + \
                            json_data.get('squareLogo', '')
                    elif json_data.get('legacyLogo', ''):
                        company_pic = 'https://media.licdn.com/media' + \
                            json_data.get('legacyLogo', '')
                    else:
                        company_pic = ''
                    company_name = json_data.get('companyName', '')
                    followers = str(json_data.get('followerCount', ''))

                    # CODE_XPATH = '//code[@id="stream-about-section-embed-id-content"]'
                    # code_text = sel.xpath(CODE_XPATH).re(r'<!--(.*)-->')
                    code_text = sel.get_element_by_id(
                        'stream-about-section-embed-id-content')
                if len(code_text) > 0:
                    code_text = str(code_text[0]).encode('utf-8')
                    code_text = re.findall(r'<!--(.*)-->', str(code_text))
                    code_text = code_text[0].strip() if code_text else '{}'
                    json_data = json.loads(code_text)
                    company_industry = json_data.get('industry', '')
                    item = {'company_name': str(company_name.encode('utf-8')),
                            'followers': str(followers),
                            'company_industry': str(company_industry.encode('utf-8')),
                            'logo_url': str(company_pic),
                            'url': str(company_data_url.encode('utf-8')), }
                    increment()

                    print(item)
                    
                    file = open('company_data.json', 'a')
                    file.write(str(item)+',\n')
                    file.close()
            except:
                pass
        else:
            pass


fetch_company_dir = fetch_request('https://www.linkedin.com/directory/companies/')

if fetch_company_dir:
    print ('Starting Company Url Scraping')
    print ('-----------------------------')
    sel = lxml.html.fromstring(fetch_company_dir.content)
    SUB_PAGES_XPATH = '//div[@class="bucket-list-container"]/ol/li/a/@href'
    sub_pages = sel.xpath(SUB_PAGES_XPATH)
    print ('Company Category URL list')
    print ('--------------------------')
    print (sub_pages)
    if sub_pages:
        for sub_page in sub_pages:
            parse_company_urls(sub_page)
else:
    pass