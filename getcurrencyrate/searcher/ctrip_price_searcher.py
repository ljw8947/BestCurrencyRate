"""
get ctrip currency rate
"""
from models import CurrencyRate
from . import base_searcher
import json
import http.client
import requests


class CtripPriceSearcher(base_searcher.BaseSearcher):
    def __init__(self):
        self.url="http://forex.ctrip.com/home/getScrollCurrencyPriceList"
    
    def getData(self):
       
        r=requests.post(self.url)
        #r.encoding
        result=r.json()["data"]["currencyList"]
        data_list=[]
        for item in result:
            data_list.append(CurrencyRate("ctrip",item["currencyCode"],item["sellPrice"],item["buyPrice"]))
        print(data_list)
        return data_list


