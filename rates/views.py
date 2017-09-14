# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django import template

import logging
import requests
import json
import datetime

logger = logging.getLogger(__name__)

# def index(request):
#     return HttpResponse("Hello, world. You're at the rates index.")
_COINS = ["BTC", "ETH", "BCH", "XRP", "LTC", "DASH", "XMR", "ETC", "ZEC", "BTS", "GNT", "SC"]

def getExchangeRate_UAH(currency):

    # today = datetime.date.today()
    # today_date = "{}.{}.{}".format(today.day, today.month, today.year)
    # request_result = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    # #https://bank.gov.ua/control/en/publish/article?art_id=25365630
    # exchangeRateList = json.loads(request_result.text)
    # for info in exchangeRateList:
    #     print(info)
    #     if info["cc"] == currency:
    #         exchangeRate = info["rate"]
    #         return exchangeRate
    return 25.5

def rates(request):
    coin = "ETH"
    request_result = requests.get('http://www.coincap.io/page/{}'.format(coin))
    averagePrice_24h = json.loads(request_result.text)["vwap_h24"]
    print(averagePrice_24h)
    getExchangeRate_UAH("USD")
    # temp = template.loader.get_template('/static/src/html/template.html')
    return HttpResponse(averagePrice_24h)
    # return render(request, '/static/src/html/template.html')
