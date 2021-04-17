#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time
import threading
import pandas as pd

from core.line_notifier import LINE_Notifier

from check_stock_method.yodobashi import Yodobashi
from check_stock_method.dummy import Dummy


class Manager:
    def __init__(self, interval_seconds=10, notify=True):
        self.interval_seconds = interval_seconds

        self.df = pd.DataFrame(
            columns=[
                "通販サイト",
                "名前",
                "在庫",
                "値段",
                "在庫確認時刻",
                "URL",
                "Method"])

        self.notify = notify
        if notify:
            self.notify_method = LINE_Notifier()
        else:
            self.notify_method = None

        self.e_commerces = {
            "yodobashi.com": Yodobashi,
            "example.com": Dummy,
        }

    def append(self, url):
        host = re.search(
            '(?:https?://)?(?P<host>.*?)(?:[:#?/@]|$)',
            url).group('host')
        e_commerce = None
        for e_commerce_url, e_commerce_method in self.e_commerces.items():
            if host.endswith(e_commerce_url):
                e_commerce = e_commerce_method
        if e_commerce is None:
            print(f"この通販サイト {host} には対応していません")
        else:
            method = e_commerce(
                url,
                notify=self.notify,
                notify_method=self.notify_method)
            self.df = self.df.append({"通販サイト": host,
                                      "名前": method.name,
                                      "在庫": method.stock,
                                      "値段": method.cost,
                                      "在庫確認時刻": method.time,
                                      "URL": url,
                                      "Method": method}, ignore_index=True)

    def update_list(self):
        self.t = threading.Timer(self.interval_seconds, self.update_list)
        self.t.start()

        # print("update_list")
        for index, row in self.df.iterrows():
            row["Method"].check_stock()

            self.df.at[index, "名前"] = row["Method"].name
            self.df.at[index, "在庫"] = row["Method"].stock
            self.df.at[index, "値段"] = row["Method"].cost
            self.df.at[index, "在庫確認時刻"] = row["Method"].time

    def start(self):
        self.t = threading.Thread(target = self.update_list)
        self.t.start()
