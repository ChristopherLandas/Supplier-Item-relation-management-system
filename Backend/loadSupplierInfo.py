
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QFont

from Utils.database import database
from Components import editSupplier



def configure_table(table: QtWidgets.QTableWidget, addHandler: bool = True):
  def cellDoubleClick(row, column):
    # print(table.item(row, 0).text())
    data = database.fetchData('Select * from supplier_info where supp_id = %s', (str(table.item(row, 0).text()), ))[0]
    editSupplier.start(lambda: configure_table(table, False), data['supplier_name'], data['address'], data['remarks'], data['stat'], str(table.item(row, 0).text()))
  
  table.clear()
  renderTable(table)

  if(addHandler):
    table.cellDoubleClicked.connect(cellDoubleClick)

def renderTable(table: QtWidgets.QTableWidget):
  data = database.fetchData("select supp_id, supplier_name as `Supplier`, case when stat = 1 then 'Active' else 'Inactive' end as `Status` from supplier_info")
  
  if len(data) > 0:
    base: list = list(data[0].keys())

    table.setColumnCount(len(base))
    table.setRowCount(len(data))

    table.setColumnHidden(0, True)

    table.setColumnWidth(1, int( table.width() * .85))
    table.setColumnWidth(2, int(table.width() * .1325))


    table.setHorizontalHeaderLabels(base)

    font = QFont()
    font.setBold(True)

    table.horizontalHeader().setMinimumHeight(40)
    for i in range(len(base)):
      table.horizontalHeaderItem(i).setFont(font)

    for x in range(len(data)):
      for y in range(len(base)):
        table.setItem(x, y, QTableWidgetItem(str(data[x][base[y]])))