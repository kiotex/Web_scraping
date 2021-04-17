#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests


class LINE_Notifier:
    def __init__(self):
        try:
            TOKEN = os.environ["LINE_TOKEN"]
            self.TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
        except KeyError:
            print("ERROR: LINE_TOKENが見つかりません(>_<)\nhttps://kino-code.com/pythonline/#toc2 を参考に、LINEのアクセストークンを取得し、環境変数'LINE_TOKEN'として設定してくださいね")

        self.api_url = 'https://notify-api.line.me/api/notify'

    def send_message(self, msg):
        send_dic = {'message': msg}
        res = requests.post(
            self.api_url,
            headers=self.TOKEN_dic,
            data=send_dic)
        if res.status_code == 200:
            print(f"メッセージ「{msg}」をLINEで送信しました")
        else:
            print(f"ERROR: メッセージ「{msg}」をLINEで送信失敗しました(>_<)")
            if res.status_code == 400:
                print("　原因：リクエストが不正")
            elif res.status_code == 401:
                print("　原因：アクセストークンが無効")
            else:
                print("　原因不明")
