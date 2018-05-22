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
