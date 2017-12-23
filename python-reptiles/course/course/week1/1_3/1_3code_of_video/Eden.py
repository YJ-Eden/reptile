# -*- coding: UTF-8 -*-
# !/usr/bin/env python
from __future__ import print_function
from bs4 import BeautifulSoup
import requests

url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#FILTERED_LIST'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')
titles = soup.select(
    '#ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.listing_info > div.listing_title > a')
images = soup.select('a.photo_link > img')
cates = soup.select(
    'div.p13n_reasoning_v2 > a > span')

for title, image, cate in zip(titles, images, cates):
    data = {
        'title': title.get_text(),
        'image': image.get('src'),
        'cate': list(cate.stripped_strings),
    }
    print(data['title'] + ',' + data['image'] + ',' + data['cate'])
