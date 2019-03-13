import sys
from PyQt5.QtWidgets import QApplication
from SSNT import SSNTWindow

app = QApplication(sys.argv)

SSNT = SSNTWindow()

sys.exit(app.exec_())
