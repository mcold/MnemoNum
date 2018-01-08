# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InsDateForm.ui'
#
# Created: Sun Dec 31 14:19:11 2017
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

class Ui_InsDateForm(object):
    def setupUi(self, InsDateForm):
        InsDateForm.setObjectName(_fromUtf8("InsDateForm"))
        InsDateForm.resize(400, 118)
        self.cmbMonth = QtGui.QComboBox(InsDateForm)
        self.cmbMonth.setGeometry(QtCore.QRect(80, 50, 221, 22))
        self.cmbMonth.setObjectName(_fromUtf8("cmbMonth"))
        self.eEvent = QtGui.QLineEdit(InsDateForm)
        self.eEvent.setGeometry(QtCore.QRect(10, 10, 381, 20))
        self.eEvent.setObjectName(_fromUtf8("eEvent"))
        self.eTag = QtGui.QLineEdit(InsDateForm)
        self.eTag.setGeometry(QtCore.QRect(10, 90, 381, 20))
        self.eTag.setObjectName(_fromUtf8("eTag"))
        self.eDay = QtGui.QLineEdit(InsDateForm)
        self.eDay.setGeometry(QtCore.QRect(10, 50, 61, 20))
        self.eDay.setObjectName(_fromUtf8("eDay"))
        self.eYear = QtGui.QLineEdit(InsDateForm)
        self.eYear.setGeometry(QtCore.QRect(310, 50, 81, 20))
        self.eYear.setObjectName(_fromUtf8("eYear"))

        self.retranslateUi(InsDateForm)
        QtCore.QMetaObject.connectSlotsByName(InsDateForm)

    def retranslateUi(self, InsDateForm):
        InsDateForm.setWindowTitle(_translate("InsDateForm", "Date", None))

