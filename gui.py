#!/usr/bin/env python3

from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

def main():
    app = QtGui.QApplication(sys.argv)
    bmi = bmi_widget()
    sys.exit(app.exec_())

class bmi_widget(QtGui.QWidget):
    def __init__(self):
        super(bmi_widget, self).__init__()

        self.initUI()

    def initUI(self):
        mainlayout = QtGui.QVBoxLayout(self)
        grid = QtGui.QGridLayout()

        length_label = QtGui.QLabel('Length (m)')
        weight_label = QtGui.QLabel('Weight (kg)')
        length_edit  = QtGui.QLineEdit()
        weight_edit  = QtGui.QLineEdit()

        calc_button  = QtGui.QPushButton('Calculate')
        # Using lambda wrapper to use callback with parameters
        calc_button.clicked.connect(lambda: self.alert_bmi(weight_edit.text(),
                                                           length_edit.text()))

        # row, column
        grid.addWidget(length_label, 0, 0)
        grid.addWidget(weight_label, 1, 0)
        grid.addWidget(length_edit,  0, 1)
        grid.addWidget(weight_edit,  1, 1)

        grid.addWidget(calc_button, 2, 1)

        self.setWindowTitle('BMI Calculator')
        #self.resize(300, 300)

        mainlayout.addLayout(grid)
        mainlayout.addStretch(1)
        #self.setLayout(grid)

        self.show()

    def alert_bmi(self, w, l):
        weight = my_float(w)
        length = my_float(l)
        QtGui.QMessageBox.about(self, 'BMI', 'Weight: %s, Length: %s' % 
                                      (weight, length))

def my_float(val):
    try:
        new_val = float(val)
    except:
        new_val = 0

    return new_val

if __name__ == '__main__':
    main()
