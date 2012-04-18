#!/usr/bin/env python

# A simple PySide example

import sys
import os
from PySide.QtCore import QObject
from PySide.QtGui import *
from PySide.QtDeclarative import *

WINDOW_TITLE = "PySide Example"

# enable running this program from absolute path
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class PropertyExample(QObject):
  """
  Python property provider
  """
  def __init__(self):
    QObject.__init__(self)


class ImagesFromPython(QDeclarativeImageProvider):
  """
  Image provider example
  """
  def __init__(self, gui):
    # this image provider supports QImage,
    # as specified by the ImageType
    QDeclarativeImageProvider.__init__(self, QDeclarativeImageProvider.ImageType.Image)

if __name__ == '__main__':
  app = QApplication(sys.argv) # create the application
  view = QDeclarativeView() # create the declarative view
  view.setSource("main.qml")

  # add Python properties to the
  # QML root context
  rc = view.rootContext()
  # add the example property
  rc.setContextProperty("example", PropertyExample())

  # register image providers
  view.engine().addImageProviders().addImageProvider("fromPython", ImagesFromPython())

  view.setWindowTitle(WINDOW_TITLE)
  view.resize(854,480)
  view.show()
  app.exec_()


