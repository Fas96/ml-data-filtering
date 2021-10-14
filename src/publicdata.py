import configparser

import pandas
from bs4 import BeautifulSoup
import requests
from openpyxl.workbook import Workbook
import os

listData = ['BUS_NODE_ID', 'BUS_STOP_ID', 'CAR_REG_NO', 'DESTINATION',
            'EXTIME_MIN', 'EXTIME_SEC', 'INFO_OFFER_TM', 'LAST_CAT',
            'LAST_STOP_ID', 'MSG_TP', 'ROUTE_CD', 'ROUTE_NO', 'ROUTE_TP', 'STATUS_POS', 'STOP_NAME']


def getAPi():
    config = configparser.RawConfigParser()
    config.read('data.properties')
    return config.get("apiSection", "api")


def connect():
    while True:
        url = getAPi()
        req = requests.get(url)
        re = req.text
        soup=BeautifulSoup(re.encode('utf-8'),'html.parser')

        for cities in soup.find_all('itemcnt'):
            print(cities)


if __name__ == '__main__':
    connect()
