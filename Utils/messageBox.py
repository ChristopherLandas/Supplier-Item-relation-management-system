from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Message(QMessageBox):
  def __init__(self, title:str, message: str, **kwargs):
    super().__init__()

    geo = self.geometry()

    self.setIcon(QMessageBox.Information)
    self.setText(message)
    self.setWindowTitle(title)
    self.setStandardButtons(QMessageBox.Ok)
    self.exec_()

class ErrorMessage(QMessageBox):
  def __init__(self, title:str, message: str, **kwargs):
    super().__init__()

    geo = self.geometry()

    self.setIcon(QMessageBox.Warning)
    self.setText(message)
    self.setWindowTitle(title)
    self.setStandardButtons(QMessageBox.Ok)
    self.exec_()


def show_warning_message(title: str, message: str) -> bool:
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)  # Set icon to Warning
    msg_box.setText(message)
    msg_box.setWindowTitle(title)
    
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    
    response = msg_box.exec_()
    
    return response == QMessageBox.Yes