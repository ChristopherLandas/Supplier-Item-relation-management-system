from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QFont

from Utils.database import database
from Utils import messageBox
from Components import addItemtoSupp

def initial(label: QtWidgets.QLabel, sup_id: str, table: QtWidgets.QTableWidget):
  supplier_name = database.execScalar('SELECT supplier_name from supplier_info where supp_id = %s', (sup_id, ))
  apos = "'" if supplier_name[-1] == 's' else "'s"
  label.setText(f'{supplier_name}{apos} Available Item/s')

  renderTable(sup_id, table)

def renderTable(sup_id: str, table: QtWidgets.QTableWidget):
  data = database.fetchData('select supplier_item_lists.siid, item_info.`name` as `Item/Product`, case when supplier_item_lists.stat = 0 then "Unavailable" when  supplier_item_lists.stat = 1 then "Available" else "Phased Out" end as `Status` from supplier_item_lists join supplier_info 	on supplier_item_lists.supp_id = supplier_info.supp_id join item_info 	on supplier_item_lists.item_id = item_info.item_id where supplier_item_lists.supp_id = %s', (sup_id, ))

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
  
def setAddItem(sup_id: str, table: QtWidgets.QTableWidget, button:QtWidgets.QPushButton):
  button.clicked.connect(lambda: addItemtoSupp.start(lambda: renderTable(sup_id, table), sup_id))