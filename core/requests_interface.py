#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import requests
from bs4 import BeautifulSoup


class Request_Interface(metaclass=ABCMeta):
    my_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP06; rv:11.0) like Gecko"
    }

    def __init__(self, url, notify=True, notify_method=None):
        self.url = url
        self.check_stock_method()
        self._last_stock = self.stock

        self.notify = notify
        if notify is True:
            if notify_method is None:
                print("ERROR: notify_method is required!")
            self.notify_method = notify_method
            self.notify_method.send_message(f"{self.url} をアサインしました")

    def get_soup(self):
        data = requests.get(self.url, headers=self.my_header)
        data.encoding = data.apparent_encoding
        return BeautifulSoup(data.text, "html.parser")

    def check_stock(self):
        """在庫確認のループ
        """
        self.check_stock_method()

        if self.stock != self._last_stock and self.stock:
            if self.notify:
                self.notify_method.send_message(f"在庫復活：{self.url}")

        self._last_stock = self.stock

    def remove_html_tags(self, text):
        """Remove html tags from a string"""
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def strip_character(self, text):
        return float(re.sub("[^0-9.]", "", self.remove_html_tags(text)))

    @abstractmethod
    def check_stock_method(self):
        """在庫確認用メソッド

        Returns:
            bool:   在庫の有無（在庫あり:True, 在庫なし:False）
            float:  金額
            string: 商品名
        """
        soup = self.get_soup()

        # do something

        self.stock = False
        self.cost = 0.0
        self.name = "product name"
