# !/usr/bin/env python
from bs4 import BeautifulSoup
import requests

'''
url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#FILTERED_LIST'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')
titles = soup.select(
    '#ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.listing_info > div.listing_title > a')
images = soup.select('a.photo_link > img')
cates = soup.select(
    'div.p13n_reasoning_v2')

for title, image, cate in zip(titles, images, cates):
    data = {
        'title': title.get_text(),
        'image': image.get('src'),
        'cate': list(cate.stripped_strings)
    }
    counts = data['cate'].count(',')
    while counts:
        data['cate'].remove(',')
        counts -= 1
    print(data)
'''

headers = {
    'Uesr-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Cookie': 'TAUnique=%1%enc%3AbFQRvXohvK%2FtODVVfcU8mwJA70bWug4zuTz1TMbjyHABS27FZ6YVQQ%3D%3D; TASSK=enc%3AAAGo8o%2BFq3pKik9p2W%2Fn83sFHKiGSjoLBVkgrOXtTp%2FIRX8%2Buj4dMh8X9%2BfYcLy2NHZPBRWhjllWxhcMHBnUWMC%2B9S3AujL0POs7zEfFs0FKwIMjjXH4pZGLIrKOYTA2UQ%3D%3D; _ym_uid=1514016407732834963; TAPD=tripadvisor.cn; __gads=ID=e89ac4c2fc80367d:T=1514016416:S=ALNI_MaBl0uGj2fapoxZOw5QkHwPYokFYQ; ServerPool=C; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.60763_358*RS.1; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPremRPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttractions-g60763-Activities-New_York_City_New_York.html; _ym_isad=2; _gat_UA-79743238-4=1; SecureLogin2=3.4%3AAP9N0DNUp88%2BDZHVeD7i9amB8nRTR865yfB6DFXVg52HTcGeHoaBPedVTPNMYhXnL9%2BMV%2B%2FZWzv0vahTM7I6kpQLAv8aYo%2B6PocwQ1ITKMMxsT1E%2BntbJ%2FFvnHmVzL8LrdTLHBtMFBn09fOhtTpGTAj6Lf0FikCRMV5xYdhiOPJScrWwa68syL9%2BAYZucKM2I3lo8eT36M0XSJhVHkHaZJg%3D; TAAuth3=3%3A8490683a36d6c77219e78d2d213d46aa%3AAJV%2Bud%2F6GlYeHiS7SF%2FvtxSPJU1T6uM60U8N9srYZH9jjN%2FK6sE%2F%2F4%2F2M5z4a%2BG9dKbpkwPiPv8uSDeSmuM591SPoEptPWsRKnpzZwzyopTDZ2jL1E8J%2F%2FpIi6g7speDa7euYvPSDlQMaSP8IOYC%2BpU2W3y9iwpAeMP2yxtNsbD2Yktyw75o2i9%2B1yfZJjItzw%3D%3D; roybatty=TNI1625!AHk7mXaY%2FraxL6HE7kfEO8Y5B9KrRsfCjCwvVCAnUlnObZDCeSpCXWQjwoIlp7%2Fs8pirErhfe35CtCbx84VK%2BIskNiFTvU0DULB47IM9RdxRJAwTcDE%2FW35y7mexj3SdUtanQW3xZUr%2BX2SjyGd4L6e4IKH%2ByfApN8YVKNfdtIwA%2C1; _ga=GA1.2.1489239506.1514016407; _gid=GA1.2.1075126758.1514016407; ki_t=1514016413763%3B1514095133205%3B1514097425130%3B2%3B10; ki_r=; TASession=%1%V2ID.EDF83F488E425AC18CBDF86DC5017993*SQ.25*LP.%2FAttractions-g60763-Activities-New_York_City_New_York%5C.html*PR.39766%7C*LS.DemandLoadAjax*GR.35*TCPAR.24*TBR.66*EXEX.13*ABTR.4*PHTB.44*FS.35*CPU.56*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.E6B5262F1193AD6CA483E18839671692*FA.1*DF.0*FLO.60763*TRA.true*LD.60763; TAUD=LA-1514095115471-1*RDD-1-2017_12_24*LG-2308826-2.1.F.*LD-2308827-.....'
}

url_saves = 'https://www.tripadvisor.cn/Saves/955927'

wb_data = requests.get(url_saves, headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')

titles = soup.select('a.title')
print(soup)
