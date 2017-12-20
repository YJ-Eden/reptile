#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function
from bs4 import BeautifulSoup

path = 'C:/Users/Administrator.ZX-201607191137/Desktop/1_2_homework_required/index.html'

with open(path, 'r') as wb_data:
    Soup = BeautifulSoup(wb_data, 'lxml')
    images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    stars = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
    reviews = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
# print(images, prices, titles, stars, reviews, sep='\n-------------------\n')

for image, price, title, star, review in zip(images, prices, titles, stars, reviews):
    data = {
        'image': image.get('src'),
        'price': price.get_text(),
        'title': title.get_text(),
        'star': len(star.find_all('span', class_='glyphicon glyphicon-star')),
        'review':review.get_text()
    }
    print(data)
