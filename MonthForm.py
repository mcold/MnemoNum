# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MonthForm.ui'
#
# Created: Sat Dec 30 19:35:18 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Months(object):
    def setupUi(self, Months):
        Months.setObjectName(_fromUtf8("Months"))
        Months.resize(279, 403)
        self.tblMonth = QtGui.QTableWidget(Months)
        self.tblMonth.setGeometry(QtCore.QRect(10, 10, 261, 391))
        self.tblMonth.setObjectName(_fromUtf8("tblMonth"))
        self.tblMonth.setColumnCount(1)
        self.tblMonth.setRowCount(12)
        item = QtGui.QTableWidgetItem()
        self.tblMonth.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblMonth.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblMonth.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblMonth.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tblMonth.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tblMonth.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tblMonth.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tblMonth.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tblMonth.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tblMonth.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tblMonth.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tblMonth.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tblMonth.setHorizontalHeaderItem(0, item)

        self.retranslateUi(Months)
        QtCore.QMetaObject.connectSlotsByName(Months)

    def retranslateUi(self, Months):
        Months.setWindowTitle(_translate("Months", "Months", None))
        item = self.tblMonth.verticalHeaderItem(0)
        item.setText(_translate("Months", "Январь", None))
        item = self.tblMonth.verticalHeaderItem(1)
        item.setText(_translate("Months", "Февраль", None))
        item = self.tblMonth.verticalHeaderItem(2)
        item.setText(_translate("Months", "Апрель", None))
        item = self.tblMonth.verticalHeaderItem(3)
        item.setText(_translate("Months", "Март", None))
        item = self.tblMonth.verticalHeaderItem(4)
        item.setText(_translate("Months", "Май", None))
        item = self.tblMonth.verticalHeaderItem(5)
        item.setText(_translate("Months", "Июнь", None))
        item = self.tblMonth.verticalHeaderItem(6)
        item.setText(_translate("Months", "Июль", None))
        item = self.tblMonth.verticalHeaderItem(7)
        item.setText(_translate("Months", "Август", None))
        item = self.tblMonth.verticalHeaderItem(8)
        item.setText(_translate("Months", "Сентябрь", None))
        item = self.tblMonth.verticalHeaderItem(9)
        item.setText(_translate("Months", "Октябрь", None))
        item = self.tblMonth.verticalHeaderItem(10)
        item.setText(_translate("Months", "Ноябрь", None))
        item = self.tblMonth.verticalHeaderItem(11)
        item.setText(_translate("Months", "Декабрь", None))
        item = self.tblMonth.horizontalHeaderItem(0)
        item.setText(_translate("Months", "Mnemo", None))

