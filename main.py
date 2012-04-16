#!/usr/bin/env python

# A simple PySide example

# enable running with absolute path
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


QML_FILE_NAME = None
WINDOW_TITLE = "PySide Example"

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *



import sys
if __name__ == '__main__':
  app = QApplication(sys.argv)
  f = QDeclarativeView()
  f.setSource("main.qml")
  f.setWindowTitle(WINDOW_TITLE)
  f.show()
  app.exec_()