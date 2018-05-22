# _*_ coding:utf-8 _*_
# Author:liu
import re
import pymysql
import requests
from bs4 import BeautifulSoup



class SearchWeather():
    def __init__(self):
        self.HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ''(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        self.CONNECTION = pymysql.connect(host='localhost', user='root', password='xxx', db='xxx', charset='utf8',
                                          cursorclass=pymysql.cursors.DictCursor)

    def getcityCode(self, cityName):
        SQL = "SELECT cityCode FROM cityWeather WHERE cityName='%s'" % cityName
        try:
            with self.CONNECTION.cursor() as cursor:
                cursor.execute(SQL)
                self.CONNECTION.commit()
                result = cursor.fetchone()
                return result['cityCode']
        except Exception as e:
            print(repr(e))
    weather = "日期      天气    【温度】    风向风力\n"
        for item in soup.find("div", {'id': '7d'}).find('ul').find_all('li'):
            date, detail = item.find('h1').string, item.find_all('p')
            title = detail[0].string
            templow = detail[1].find("i").string
            temphigh = detail[1].find('span').string if detail[1].find('span') else ''
            wind, direction = detail[2].find('span')['title'], detail[2].find('i').string
            if temphigh == '':
                weather += '你好，【%s】今天白天：【%s】，温度：【%s】，%s：【%s】\n' % (cityname, title, templow, wind, direction)
            else:
                weather += (date + title + "【" + templow + "~" + temphigh + '°C】' + wind + direction + "\n")
        return weather

    def main(self, city):
        cityCode = self.getcityCode(city)
        detail = self.getWeather(cityCode, city)
        print(detail)


if __name__ == "__main__":
    weather = SearchWeather()
