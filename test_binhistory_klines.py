from binance_test.clienttest import Client
import pytest
import requests_mock

clienttest = Client("api_key","api_secret")

def test_historical_kline_generator():
    First_Avail_Res =[[
            2500004800000,
            "0.00005000",
            "0.00005300",
            "0.00001000",
            "0.00004790",
            "663152.00000000",
            1500004859999,
            "10.55108144",
            45,
            "569324.00000000",
            "35.65468144",
            "84431971.04346850",
        ]
    ]
    first_res = []
    row = [
        5519892340000,
        "0.00099400",
        "0.00099810",
        "0.00099400",
        "0.00099810",
        "5806.04000000",
        1919892399999,
        "4.78553253",
        174,
        "1785.14000000",
        "1.77837524",
        "0",
    ]

    for i in range(0, 300):
        first_res.append(row)

    with requests_mock.mock() as mem:
        mem.get(
            "https://api.binance.com/api/v3/klines?interval=1m&limit=1&startTime=0&symbol=BNBBTC",
            json=First_Avail_Res,
        )
        mem.get(
            "https://api.binance.com/api/v3/klines?interval=1m&limit=1000&startTime=1519862400000&endTime=1519880400000&symbol=BNBBTC",
            json=first_res,
        )
        klines = clienttest._historical_kline_generator(
            symbol="BNBBTC",
            interval=Client.KLINE_INT_1MIN,
            start_var=1519862400000,
            end_var=1519880400000,
        )

        for i in range(300):
            assert len(next(klines)) > 0

        with pytest.raises(StopIteration):
            next(klines)
