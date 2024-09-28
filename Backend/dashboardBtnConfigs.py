import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QFont

from Utils.database import database
from Components import addItem as popup
from Components import addSupplier as popup1

def addItem(item_btn: QtWidgets.QPushButton, callback: callable):
  if(item_btn is not None):
    item_btn.clicked.connect(lambda: popup.start(callback))

def addSupplier(supplier_btn: QtWidgets.QPushButton, callback: callable):
  if supplier_btn is not None:
    supplier_btn.clicked.connect(lambda: popup1.start(callback))