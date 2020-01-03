import sys
from gui.node import Node
from gui.treemodel import TreeModel
from PyQt4 import QtGui
from lxml import etree
from vssbackup.vss_backup_explorer import VSSBackupExplorer


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.tree = QtGui.QTreeView()
        self.directory = QtGui.QLabel()
        self.button = QtGui.QPushButton('Select Directory', self)
        self.directory.setText("Select")
        self.button.clicked.connect(self.select_dir)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.directory)
        layout.addWidget(self.tree)

    def select_dir(self):
        dir_selected = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        if dir_selected is not None and dir_selected is not "":
            self.directory.setText(dir_selected)
            self.show_tree(dir_selected)

    @staticmethod
    def show_error(message):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Critical)
        msg.setText("Encountered error while reading files in directory")
        msg.setInformativeText("See details")
        msg.setWindowTitle("Error")
        msg.setDetailedText(message)
        msg.exec_()

    def show_tree(self, dir):
        file_tree = Node("Root")
        try:
            explorer = VSSBackupExplorer(dir + "/")
            xml = explorer.process()
            #TODO Fix this hack that removes xmlns from FILE_GROUP
            xml = xml.replace("xmlns=\"x-schema:#VssWriterMetadataInfo\"", "")
            root = etree.fromstring(xml)
            # TODO 1: need to handle EXCLUDE_FILES
            backup_files = root.findall('./FILE_GROUP/FILE_LIST')
        except Exception as ex:
            self.show_error(str(ex))
            return

        for backup_file in backup_files:
            path = backup_file.get("path")
            file_name = backup_file.get("filespec")
            recursive = backup_file.get("recursive", False)
            if not recursive:
                # TODO 2: need to handle recursive
                full_file_name = path.lower() + "\\" + file_name.lower()
                self._add_to_tree(file_tree, full_file_name)
        model = TreeModel(file_tree)
        self.tree.setModel(model)

    def _add_to_tree(self, file_tree, file_name):
        path_components = file_name.split("\\")
        current_node = file_tree
        for path_component in path_components:
            current_node = self._get_child_node(path_component, current_node)

    @staticmethod
    def _get_child_node(next_node_name, current_node):
        # Gets child node or creates new
        child = current_node.get_child(next_node_name)
        if not child:
            child = Node(next_node_name, current_node)
        return child


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(["VSS Backup"])
    window = Window()
    window.show()
    sys.exit(app.exec_())