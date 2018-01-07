# !/usr/bin/env python
from bs4 import BeautifulSoup
import requests
import time

url = 'https://zh.airbnb.com/rooms/9040671?location=%E4%B8%AD%E5%9B%BD%E5%8C%97%E4%BA%AC%E5%B8%82&s=BN6hYkm9'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')

title = soup.select('div._13nd2f7d')[0].text
loc = soup.select('div._ew0cqip')[0].text
img = soup.select('div._fi92kxy')[0].get('style')
# landlord_img = soup.select('div._ncmdki > div > div > button > img')[0].get('src')
# landlord_name = soup.select('span._itxyqmm')[0].text

print('民宿名字：', title)
print('地址：', loc)
print('图片地址：', img)
# print('房主头像：', landlord_img)
# print('房主昵称：', landlord_name)
