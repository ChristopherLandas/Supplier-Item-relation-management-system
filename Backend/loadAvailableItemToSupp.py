from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QFont

from Utils.database import database
from Components import editItem
from Utils import messageBox

def initial(sup_id: str, table: QtWidgets.QTableWidget):
  renderTable(sup_id, table)

def renderTable(sup_id: str, table: QtWidgets.QTableWidget):
  data = database.fetchData('select item_id, `name` as `Name`, CONCAT("₱", FORMAT(base_price,2)) as Price from item_info where item_id not in (select item_id from supplier_item_lists where supp_id = %s)', (sup_id, ))
  
  if len(data) > 0:
    base: list = list(data[0].keys())

    table.setColumnCount(len(base))
    table.setRowCount(len(data))

    table.setColumnHidden(0, True)

    table.setColumnWidth(1, int( table.width() * .85))
    table.setColumnWidth(2, int(table.width() * .1325))


    table.setHorizontalHeaderLabels(base)

    font = QFont()
    font.setPointSize(14)
    font.setBold(True)

    table.horizontalHeader().setMinimumHeight(40)
    for i in range(len(base)):
      table.horizontalHeaderItem(i).setFont(font)

    for x in range(len(data)):
      for y in range(len(base)):
        table.setItem(x, y, QTableWidgetItem(str(data[x][base[y]])))

  else:
      messageBox.Message("No Item/s to add", "All Items on the lists are available to the supplier")
      table.setColumnCount(0)
      table.setRowCount(0)