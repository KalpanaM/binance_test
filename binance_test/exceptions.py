import json

class binancetestAPIException(Exception):
    def __init__(self, res, stat, msg):
        self.code=0
        try:
            json_res =json.loads(msg)
        except ValueError:
            self.message = 'Invalid message from Binance{}'.format(res.msg)
        else:
            self.code =json_res.get('code')
            self.message =json_res.get('msg')
class binancetestOrderException(Exception):
    def __init__(self,code,message):
        self.code=code
        self.message=message

    def __str__(self):
        return 'BinancetestOrderException' % (self.code,self.message)

class binancetestSymbolException(binancetestOrderException):
    def __init__(self,value):
        message = "Invalid Symbol" %value
        super().__init__(1000,message)
class binancetestUnableToGet(binancetestOrderException):
    pass

class NotImplementedException(Exception):
    def __init__(self, value):
        message = f'Not implemented@{value}'
        super().__init__(message)

class binancetestRequestException(Exception):
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return 'BinancetestRequestException' % (self.message)



