#!/usr/bin/env python

# A simple PySide example

import sys
import os
from PySide.QtGui import *
from PySide.QtDeclarative import *

WINDOW_TITLE = "PySide Example"

# enable running this program from absolute path
os.chdir(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
  app = QApplication(sys.argv) # create the application
  view = QDeclarativeView() # create the declarative view
  view.setSource("main.qml")
  view.setWindowTitle(WINDOW_TITLE)
  view.resize(854,480)
  view.show()
  app.exec_()