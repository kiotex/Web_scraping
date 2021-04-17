#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import random
import datetime
from core.requests_interface import Request_Interface

class Dummy(Request_Interface):
    base_url = "example.com"
    site = "ダミー通販サイト"

    def __init__(self, url, notify=True, notify_method=None):
        super().__init__(url, notify, notify_method)
        self.check_stock_method()


    def check_stock_method(self):
        """在庫確認用メソッド

        Returns:
            bool:   在庫の有無（在庫あり:True, 在庫なし:False）
            float:  金額
            string: 商品名
        """

        print(self.time, self.url)

        self.stock = bool(random.getrandbits(1))

        self.cost = random.randint(100,10000)
        self.name = re.findall(r'(?:https?://)?(.*)/(.*)/',self.url)[0][1]

        self.time = datetime.datetime.now()
