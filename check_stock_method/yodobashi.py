#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.requests_interface import Request_Interface

class Yodobashi(Request_Interface):
    def __init__(self, url, notify=True, notify_method=None):
        super().__init__(**kwargs)

    def check_stock_method(self):
        """在庫確認用メソッド

        Returns:
            bool:   在庫の有無（在庫あり:True, 在庫なし:False, ERROR: -1）
            float:  金額
            string: 商品名
        """
        soup = self.get_soup()
        cost = self.strip_character(soup.select_one("#js_scl_unitPrice").text)
        name = self.remove_html_tags(soup.select_one("#products_maintitle").text)
        if soup.select_one("#salesInfoTxt").text == "在庫あり":

            return True, cost, name
        else:
            return False, cost, name
