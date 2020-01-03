# This example from https://github.com/pyqt/examples/tree/_/src/12%20QTreeView%20example%20in%20Python
from os.path import expanduser
# Original example using qt5 so change the following line
#from PyQt5.QtWidgets import *
from PyQt4.QtGui import *

home_directory = expanduser('~')

app = QApplication([])
model = QDirModel()
view = QTreeView()
view.setModel(model)
view.setRootIndex(model.index(home_directory))
view.show()
app.exec_()

