#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function
from bs4 import BeautifulSoup

with open('C:/Users/Administrator.ZX-201607191137/Desktop/1_2_homework_required/index.html', 'r') as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    # print(Soup)

    titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    # stars特殊，需要取所有同类标签
    stars = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
    reviews = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
# print(stars, stars2, sep='\n-------------------\n')

for title, price, star, review, image in zip(titles, prices, stars, reviews, images):
    data = {
        'title': title.get_text(),
        'price': price.get_text(),
        'star': len(star.find_all('span', class_='glyphicon glyphicon-star')),
        'review': review.get_text(),
        'image': image.get('src')
    }
    print(data)

