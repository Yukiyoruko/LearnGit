# -*- coding:utf-8 -*-
# MyfirstPyScript
# coded by Yo1uk0

import requests
# from bs4 import BeautifulSoup
import json

path = "/mnt/c/workplace"
url = "https://api.bilibili.com/x/space/arc/search?mid=231590&ps=30&tid=0&pn=1&keyword=&order=click&jsonp=jsonp"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.110 Safari/537.36',
    'referer': 'https://space.bilibili.com/231590/video'}


def find_url(url0, num0):
    web = requests.get(url0)
    data = json.loads(web.text)
    data1 = data["data"]["list"]["vlist"][num0]["pic"]
    return data1


def download(url1, download_num):
    # 字符串替換，將url裏的.webp去掉（可惡，因爲是Ajax的動態網頁用不到了）
    # url0 = format(url1.replace('@640w_400h_100Q_1c.webp', ''))
    # 請求頁面
    jpg = requests.get(url1, headers=headers)
    f = open("azusa" + str(download_num) + ".jpg", 'wb')
    f.write(jpg.content)
    f.close()
    print('Pic saved!')


def main():
    for num in range(30):
        url1 = find_url(url, num)
        download(url1, num)
    print('all pics are saved!')


if __name__ == '__main__':
    main()
# def find(url):
# web = requests.get(url, headers=headers)
# html = web.content.decode("utf-8")
# print(web.status_code)
# 取得網頁內容
# soup = BeautifulSoup(html, "lxml")
# 轉換成標籤樹 找頁面内DOM參數
# lis = soup.find_all('li', class_="small-item fakeDanmu-item")
# print(lis)
# print(soup.find_all('li'))
# print(soup.find_all('a', class_="cover"))
# print(soup.find_all('li', class_="small-item fakeDanmu-item"))
# print(soup.find_all('a')[0]['href'])
# url0 = lis[1].a.img['src']
# url1 = 'http://'+url0
# print(url1)
# print(html)
