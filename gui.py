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
        self.setWindowTitle('BMI Calculator')

        # Creating elements

        mainlayout = QtGui.QVBoxLayout(self)
        grid = QtGui.QGridLayout()

        length_label = QtGui.QLabel('Length (m)')
        weight_label = QtGui.QLabel('Weight (kg)')
        length_edit  = QtGui.QLineEdit()
        weight_edit  = QtGui.QLineEdit()
        
        calc_button  = QtGui.QPushButton('Calculate')
        
        bmi_label  = QtGui.QLabel('BMI:')
        bmi_result = QtGui.QLabel('0')

        # Create events
        # Using lambda wrapper to use callback with parameters
        calc_button.clicked.connect(lambda: self.alert_bmi(weight_edit.text(),
                                                           length_edit.text(),
                                                           bmi_result))

        weight_edit.returnPressed.connect(lambda: self.alert_bmi(weight_edit.text(),
                                                           length_edit.text(),
                                                           bmi_result))

        # Place elements (row, column)
        grid.addWidget(length_label, 0, 0)
        grid.addWidget(weight_label, 1, 0)
        grid.addWidget(length_edit,  0, 1)
        grid.addWidget(weight_edit,  1, 1)
        grid.addWidget(bmi_label,    3, 0)
        grid.addWidget(bmi_result,   3, 1)

        grid.addWidget(calc_button, 2, 1)

        mainlayout.addLayout(grid)
        mainlayout.addStretch(1)

        self.show()

    def alert_bmi(self, w, l, bmi):
        weight = my_float(w)
        length = my_float(l)

        bmi.setText("{0:2.1f}".format(weight / (length * length)))
        #QtGui.QMessageBox.about(self, 'BMI', 'Weight: %s, Length: %s' %
        #                              (weight, length))

def my_float(val):
    try:
        float_val = float(val)
    except:
        float_val = 0

    return float_val


if __name__ == '__main__':
    main()
