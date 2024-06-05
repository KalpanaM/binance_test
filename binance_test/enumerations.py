from enum import Enum

KLINE_INT_1SEC= '1s'
KLINE_INT_1MIN= '1m'

ORD_STAT_NEW = 'NEW'
ORD_STAT_CANCEL = 'CANCELLED'
ORD_STAT_EXP = 'EXPIRED'

class BinanceKlines(Enum):
        BID = 1
        QUOTE = 2
        FUTURES =3
        OPTIONS =4
