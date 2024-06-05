from binance_test.clienttest import Client
from binance_test.exceptions import binancetestAPIException, binancetestRequestException, NotImplementedException

import pytest
import requests_mock

clienttest = Client("api_key","api_secret")

def test_false_validation_json():
    with pytest.raises(binancetestRequestException):
        with requests_mock.mock() as mem:
            mem.get("https://www.binance.com/exchange-api/v1/public/asset-service/product/get-products",text="<head></html>",)
            clienttest.get_products()
def test_API_Exception():
    with pytest.raises(binancetestAPIException):
        with requests_mock.mock() as mem:
            json_object ={"code":1002, "message":"Invalid API Request"}
            mem.get("https://api.binance.com/api/v3/time",json=json_object,status_code=400)
            clienttest.get_server_time()

def test_API_Exception_Invalid_JSON():
    with pytest.raises(binancetestAPIException):
        with requests_mock.mock() as mem:
            not_json ="<html><body>Error</body></html>"
            mem.get("https://api.binance.com/api/v3/time",text=not_json,status_code=400)
            clienttest.get_server_time()
