#!/usr/bin/env python

# A simple PySide example

import sys
import os
import traceback

# log to file on Android

LOG_FOLDER = '/sdcard/'
fSock = open(os.path.join(LOG_FOLDER, 'pyside_example_log.txt'), 'w', 0)
rfSock = open(os.path.join(LOG_FOLDER, 'pyside_example_error_log.txt'), 'w', 0)
sys.stdout = fSock
sys.stderr = rfSock

print("** stdout diverted to file **")

# for some reason, the PySide bindings can't find the libshiboken.so and libshiboken,
# even though they are in a directory in LD_LIBRARY_PATH, resulting in errors like this:
#
# ImportError: Cannot load library: link_image[1965]:   157 could not load needed library
# 'libshiboken.so' for 'QtCore.so' (load_library[1120]: Library 'libshiboken.so' not found)
#
# if both are loaded to memory manually with ctypes, everything works fine
print('manual libshiboken.so and libpyside.so loading')
from ctypes import *
PROJECT_FOLDER = '/data/data/org.modrana.PySideExample'
LIB_DIR = os.path.join(PROJECT_FOLDER, 'files/python/lib')
SHIBOKEN_SO = os.path.join(LIB_DIR, 'libshiboken.so')
PYSIDE_SO = os.path.join(LIB_DIR, 'libpyside.so')
print("path to libshiboken and libpyside:")
print(SHIBOKEN_SO)
print(PYSIDE_SO)
shibok = CDLL(SHIBOKEN_SO)
psde = CDLL(PYSIDE_SO)
print("manual loading done")

print("importing PySide")
from PySide import QtCore, QtGui
from PySide.QtCore import QObject
from PySide.QtGui import *
from PySide.QtDeclarative import *
print("PySide import done")

#print(os.environ)

import datetime

WINDOW_TITLE = "PySide@Android Example"

# enable running this program from absolute path
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("dir changed")

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
    image = QImage("pyside.png")
    image.scaled(requestedSize.width(),requestedSize.height())
    painter = QtGui.QPainter(image)
    painter.setPen("white")
    painter.drawText(20, 20, text)
    return image

def main():
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


  view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
  view.setSource("main.qml")
  rootObject = view.rootObject()
  property.rootObject = rootObject

  view.setWindowTitle(WINDOW_TITLE)
  # view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
  #view.setResizeMode(QDeclarativeView.SizeViewToRootObject)
  view.window().showFullScreen()
  # view.resize(480,854)
  #view.resize(854,480)
  view.show()
  app.exec_()



if __name__ == '__main__':
  print("__main__")
  fSock.flush()
  try:
    main()
  except Exception:
    fp = open(os.path.join(LOG_FOLDER, 'pyside_example_exception_log.txt'), 'w', 0)
    traceback.print_exc(file=fp)
    fp.flush()
    fp.close()
    traceback.print_exc(file=fSock)
    fSock.flush()
  fSock.flush()
  fSock.close()
  exit(0)


