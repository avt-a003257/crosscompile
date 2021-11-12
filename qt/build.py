import os, sys

if sys.version_info.major < 3:
  sys.exit("Bad Python version < 3");

import wget, tarfile

MAJOR = 4.8
MINOR = 7
VERSION = str(MAJOR) + '.' + str(MINOR)
FILENAME = 'qt-everywhere-opensource-src-' + str(VERSION) + '.tar.gz'
URL = 'https://download.qt.io/archive/qt/' + str(MAJOR) + '/' + str(VERSION) + '/' + FILENAME

if False == os.path.isfile(FILENAME):
  wget.download(URL)
else:
  print(FILENAME + ' already exists')
  
