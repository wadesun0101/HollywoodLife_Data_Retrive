# -*- coding: utf-8 -*-

import urllib3
from bs4 import BeautifulSoup
import csv
from datetime import datetime

http = urllib3.PoolManager()

quote_page = ["http://hollywoodlife.com/2018/05/20/prince-harry-meghan-markle-body-language-royal-wedding-love-meaning/"]

data = []

for hl in quote_page:
    page = http.request('GET',hl)
    soup = BeautifulSoup(page.data, "lxml")
    title_box = soup.find('meta', attrs={'property':'og:title'})
    title = title_box['content']
    url_box = soup.find('meta', attrs={'property':'og:url'})
    url = url_box['content']
    author_box = soup.find('meta', attrs={'name':'author'})
    author = author_box['content']
    tag_box = soup.find('meta', attrs={'name':'news_keywords'})
    tag = tag_box['content']
    data.append((title,url,author,tag))
    
with open('Page_detail.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 for title, url, author, tag in data:
     writer.writerow([title, url,author, tag, datetime.now()])




    

    
    

    