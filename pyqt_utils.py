#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@file pyqt_utils.py
@version 0.0.1
@author naisoa
@brief gui with pyqt5
"""
import os
import sys
import access_nem_node
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # set parts
        self.set_button()
        self.set_price_area()
        self.set_layout()
        # set main window
        self.setGeometry(0, 0, 300, 150)
        self.setWindowTitle('Graphic User Interface')

    def get_param(self):
        # access zaif api
        # print("wallet xem amount[-]: %2f, jpy/xem[en]: %2f, total price[en]: %2f" % (amount, exchange_jpy, price))
        node = "http://hugealice.nem.ninja:7890" 
        wallet_address = "NAGJG3QFWYZ37LMI7IQPSGQNYADGSJZGJRD2DIYA"
        access = access_nem_node.Access(node, wallet_address)   
        amount, exchange_jpy, price = access.get_xem_price()
        # set zaif param
        self.zaif_amount = amount
        self.zaif_exchange = exchange_jpy
        self.zaif_price = price
        # access my wallet
        node = "http://hugealice.nem.ninja:7890" 
        wallet_address = "NDQUDJ3LHJVVU27APQ4PZS4I2CQDO6ANGTWUGBDT"
        access = access_nem_node.Access(node, wallet_address)   
        amount, exchange_jpy, price = access.get_xem_price()
        # set my wallet param
        self.wallet_amount = amount
        self.wallet_exchange = exchange_jpy
        self.wallet_price = price

    def set_button(self):
        # create radio_button_zaif
        self.radio_button_zaif = QRadioButton("zaif")
        self.radio_button_zaif.setCheckable(True)
        self.radio_button_zaif.setFocusPolicy(Qt.NoFocus)
        # create radio_button_wallet
        self.radio_button_wallet = QRadioButton("my_wallet")
        self.radio_button_wallet.setCheckable(True)
        self.radio_button_wallet.setFocusPolicy(Qt.NoFocus)
        # set horizon layout
        self.layout_button = QHBoxLayout()
        self.layout_button.addWidget(self.radio_button_zaif)
        self.layout_button.addWidget(self.radio_button_wallet)
        # set action
        self.radio_button_zaif.clicked.connect(self.clicked)
        self.radio_button_wallet.clicked.connect(self.clicked)

    def set_price_area(self):
        # create label
        self.label_amount = QLabel("     xem amount")
        self.label_exchange = QLabel("    jpy/xem[yen]")
        self.label_price = QLabel("total price[yen]")
        # create edit
        self.edit_amount = QLineEdit()
        self.edit_exchange = QLineEdit()
        self.edit_price = QLineEdit()
        # set horizon layout
        self.layout_amount = QHBoxLayout()
        self.layout_amount.addWidget(self.label_amount)
        self.layout_amount.addWidget(self.edit_amount)
        self.layout_exchange = QHBoxLayout()
        self.layout_exchange.addWidget(self.label_exchange)
        self.layout_exchange.addWidget(self.edit_exchange)
        self.layout_price = QHBoxLayout()
        self.layout_price.addWidget(self.label_price)
        self.layout_price.addWidget(self.edit_price)

    def set_layout(self):
        # add layout
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.layout_button)
        self.layout.addLayout(self.layout_amount)
        self.layout.addLayout(self.layout_exchange)
        self.layout.addLayout(self.layout_price)
        self.setLayout(self.layout)

    def clicked(self):
        # get param
        self.get_param()
        # set edit
        radio_button = self.sender()
        if radio_button.text() == "zaif":
            self.edit_amount.setText(str(self.zaif_amount))
            self.edit_exchange.setText(str(self.zaif_exchange))
            self.edit_price.setText(str(self.zaif_price))
        elif radio_button.text() == "my_wallet":
            self.edit_amount.setText(str(self.wallet_amount))
            self.edit_exchange.setText(str(self.wallet_exchange))
            self.edit_price.setText(str(self.wallet_price))
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
