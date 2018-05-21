# -*- coding: utf-8 -*-
"""
Created on Mon May 21 09:10:49 2018

@author: Wade Sun
"""
# First of all, retrive the data from Hollywoodlife post api and export to a .txt file.
# Second, create headers for each record.
# Last but not least, get the selected data and export to csv file.

import os
import csv
import json

url_link = "https://public-api.wordpress.com/wp/v2/sites/hollywoodlife.com/posts"

from urllib.request import urlopen

with urlopen(url_link) as url:
    data = url.read()

# Download the webpage as json file .
    
filename = "posts_Hollywood_Life.txt"
file_ = open(filename, 'wb')
file_.write(data)
file_.close()

# 
def export_csv_file (fn, row, fieldnames):
    if (os.path.isfile(fn)):
        m = "a"
    else:
        m = "w"
        
    with open(fn, m, encoding="utf-8", newline='')as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        if (m == "w"):
            writer.writeheader()
        writer.writerow(row)
        
with open(filename) as json_file:
    json_data = json.load(json_file)
    
for n in json_data:
    h = {}
    h["POST_ID"] = n['id']
    h["Title"] = n['title']['rendered']
    h["URL"] = n['guid']['rendered']
    h["Author"] = n['author']
    h["Category"] = n['categories']
    h["Tags"] = n['tags']
    h["Date"] = n['date']

    export_csv_file ("Hollywood_Life.csv", h, ['POST_ID', 'Title', 'URL', 'Author', 'Category', 'Tags', 'Date'])
    
    