import asyncio
import logging
import json
import time
from asyncio import sleep
from enum import Enum
from typing import Optional, Tuple, List

import websockets as ws

class BinanceTestSocketManager:
    STREAM_URL = 'wss://ws-api.binance.{}:9443/'

    def __init__(self):
        self.STREAM_URL = self.STREAM_URL.format()