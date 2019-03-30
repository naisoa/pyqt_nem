#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@file main.py
@version 0.0.1
@author naisoa
@brief it's access function to nem nodes
"""
import requests
import json

class Access:
    def __init__(self, node, wallet_address):
        api = '/account/get'
        self.url = str(node + api + '?' + 'address=' + wallet_address)
        self.zaif_xem_api = 'https://api.zaif.jp/api/1/ticker/xem_jpy'

    def get_xem_price(self):
        # access nem node 
        # details:print(json.dumps(wallet,indent=4))
        wallet = requests.get(self.url).json()

        # access nem zaif 
        # details:print(json.dumps(xem_exchange,indent=4))
        xem_exchange = requests.get(self.zaif_xem_api).json()
        
        # get xem price
        xem_amount = wallet['account']['balance'] / 1000000
        xem_jpy = xem_exchange['vwap']
        xem_price = xem_amount * xem_jpy
        return xem_amount, xem_jpy, xem_price

