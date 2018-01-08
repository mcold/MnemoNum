# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RetypeForm.ui'
#
# Created: Tue Jan 02 00:04:13 2018
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

class Ui_RetypeForm(object):
    def setupUi(self, RetypeForm):
        RetypeForm.setObjectName(_fromUtf8("RetypeForm"))
        RetypeForm.resize(153, 77)
        self.eNum = QtGui.QLineEdit(RetypeForm)
        self.eNum.setGeometry(QtCore.QRect(10, 20, 131, 20))
        self.eNum.setObjectName(_fromUtf8("eNum"))
        self.lblCounter = QtGui.QLabel(RetypeForm)
        self.lblCounter.setGeometry(QtCore.QRect(20, 50, 121, 16))
        self.lblCounter.setText(_fromUtf8(""))
        self.lblCounter.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCounter.setObjectName(_fromUtf8("lblCounter"))

        self.retranslateUi(RetypeForm)
        QtCore.QMetaObject.connectSlotsByName(RetypeForm)

    def retranslateUi(self, RetypeForm):
        RetypeForm.setWindowTitle(_translate("RetypeForm", "Retype", None))

