from PyQt5 import QtWidgets
from SSNT_ui import Ui_SSNT

class SSNTWindow(QtWidgets.QWidget, Ui_SSNT):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Connect buttons

        self.pushButton_copy.clicked.connect(self.copyText)

        self.pushButton_clear.clicked.connect(self.clearText)

        self.pushButton_save.clicked.connect(self.saveText)

        self.toolButton_filepath.clicked.connect(self.filePath)

    def copyText(self):
        print("Copy")

    def clearText(self):
        print("Clear")

    def saveText(self):
        print("Save")

    def filePath(self):
        print("Get File Path")
