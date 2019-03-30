#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@file main.py
@version 0.0.1
@author naisoa
@brief it's main function for nem access gui  
"""
import pyqt_utils
import sys
import json
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = pyqt_utils.MainWindow()
    main_window.show()
    sys.exit(app.exec_())