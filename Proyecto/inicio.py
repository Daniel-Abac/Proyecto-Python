#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: donald
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from temp import Ui_mainWindow
app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
