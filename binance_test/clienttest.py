from typing import Dict, List, Tuple, Optional, Any
import asyncio
import requests
import time

from .exceptions import binancetestAPIException,binancetestRequestException,binancetestOrderException,binancetestSymbolException, NotImplementedException
from .enumerations import BinanceKlines

class BinanceClient:
    WEBAPI_URL =' https://api.binance.com/api/v3/depth?symbol=BNBBTC&limit=1000'
    WEB_URL ='https://www.binance.{}'

    KLINE_INT_1SEC = '1s'
    KLINE_INT_1MIN = '1m'

    ORD_STAT_NEW = 'NEW'
    ORD_STAT_CANCEL = 'CANCELLED'
    ORD_STAT_EXP = 'EXPIRED'

class Client(BinanceClient):

    def __init__(self,api_key: Optional[str]=None, api_secret: Optional[str]=None, tld:str ='com',requests_params:Optional[Dict[str,Any]]=None):
        self.tld=tld
        self.WEB_URL =self.WEB_URL.format(tld)
        self.WEBAPI_URL=self.WEBAPI_URL.format(tld)
        self.session =self._init_session()
        self.response=None


    def _init_session(self) ->requests.Session:
        #headers =self._get_headers()
        session= requests.session()
       # session.headers.update(headers)
        return session

    def get_products(self) -> Dict:
        products =self._request_website('get','bapi/asset/v2/public/asset-service/product/get-products?includeEtf=true')
        return products

    def get_symbol_detail(self, symbol) -> Optional[Dict]:
        res =self.get_symbol_detail()
        for item in res['symbols']:
            if item['symbol'] == symbol.upper():
                return item
        return None
    def get_server_time(self):
        #return binancetestRequestException,binancetestAPIException
        return self._get('time', version=3)
    def _klines(self,klines_type: BinanceKlines = BinanceKlines.BID) -> Dict:
        if BinanceKlines.BID == klines_type:
            return self._klines(self)
        else:
            #raise Exception
            pass
    def _historical_kline_generator(self, symbol, interval, start_var=None, end_var=None, limit=1000, klines_type : BinanceKlines = BinanceKlines.BID):
    # return self._historical_kline_generator(symbol,interval,start_var,end_var,limit,klines_type=klines_type)

        test_id = 0
        while True:
            output_data = self._klines(
                klines_type=klines_type,
                #symbol=symbol,

            )
            if output_data:
                for ii in output_data:
                    yield ii

           # if not len(output_data) or len(output_data) < limit:
               # break
            test_id += 1
            if test_id % 2 == 0:
                 time.sleep(1)



