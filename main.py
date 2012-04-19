#!/usr/bin/env python

# A simple PySide example
from PySide import QtCore, QtGui

import sys
import os
from PySide.QtCore import QObject
from PySide.QtGui import *
from PySide.QtDeclarative import *
import time
import datetime

WINDOW_TITLE = "PySide Example"

# enable running this program from absolute path
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class PropertyExample(QObject):
  """
  Python property provider
  """
  def __init__(self):
    QObject.__init__(self)
    self.rootObject = None
    #NOTE: the root object is needed only by Python properties
    # that call QML code directly

  @QtCore.Slot(result=str)
  def getDate(self):
    """
    return current date & time
    """
    return str(datetime.datetime.now())

  @QtCore.Slot(str)
  def notify(self, text):
    """
    trigger a notification using the
    Qt Quick Components InfoBanner
    """

    #NOTE: QML uses <br> instead of \n for linebreaks
    self.rootObject.notify(text)



class ImagesFromPython(QDeclarativeImageProvider):
  """
  Image provider example
  """
  def __init__(self):
    # this image provider supports QImage,
    # as specified by the ImageType
    QDeclarativeImageProvider.__init__(self, QDeclarativeImageProvider.ImageType.Image)

  def requestImage(self, pathId, size, requestedSize):
    # we ignore size & requested size for simplicity

    # we use the path ID provided from the URL used
    # in QML for a caption to paint on the image
    text = pathId

    # for an example image, PySide logo in SVG is used
    image = QImage("pyside.svg")
    image.scaled(requestedSize.width(),requestedSize.height())
    painter = QtGui.QPainter(image)
    painter.setPen("white")
    painter.drawText(20, 20, text)
    return image

if __name__ == '__main__':
  app = QApplication(sys.argv) # create the application
  view = QDeclarativeView() # create the declarative view
  # add Python properties to the
  # QML root context
  rc = view.rootContext()
  # add the example property
  property = PropertyExample()
  rc.setContextProperty("example", property)

  # register image providers
  # NOTE: the image provider name in the Image.source URL is automatically lower-cased !!
  provider = ImagesFromPython()
  view.engine().addImageProvider("from_python", provider)
  # NOTE2: view.engine().addImageProvider("from_python", ImagesFromPython())
  # doesn't work for some reason

  view.setSource("main.qml")
  rootObject = view.rootObject()
  property.rootObject = rootObject

  view.setWindowTitle(WINDOW_TITLE)
  view.resize(480,854)
  #view.resize(854,480)
  view.show()
  app.exec_()


