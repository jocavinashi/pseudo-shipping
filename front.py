import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator, QTextBlock

from PyQt5.QtWidgets import *
from distance import input ,price_calculator
# from PyQt5.QtWidgets import QLabel
# from PyQt5.QtWidgets import QWidget

# app = QApplication(sys.argv)
class Dialog(QDialog):
    """Dialog."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Shipping calculator')
        self.form=QLineEdit()
        self.to=QLineEdit()
        self.weight=QLineEdit()
        self.unit=QLineEdit()
        self.by=QLineEdit()
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('From:',self.form)
        formLayout.addRow('To:',self.to)
        formLayout.addRow('Weight:', self.weight)
        formLayout.addRow('Units:', self.unit)
        formLayout.addRow('by:', self.by)
        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)

class Output(QDialog):     
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle('Shipping calculator output')
        abc=input(dlg.form.text(),dlg.to.text(),dlg.weight.text(),dlg.unit.text().upper(),dlg.by.text().lower())
        label =QtWidgets.QLabel(abc,self)
        label.setText(abc)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    # import pdb;pdb.set_trace()
    if dlg.exec():
        out=Output()
        out.resize(600, 100)
        out.show()

    sys.exit(app.exec_())
    