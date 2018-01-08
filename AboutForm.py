# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutForm.ui'
#
# Created: Sat Dec 30 17:58:15 2017
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

class Ui_frmAbout(object):
    def setupUi(self, frmAbout):
        frmAbout.setObjectName(_fromUtf8("frmAbout"))
        frmAbout.resize(458, 74)
        self.lblAbout = QtGui.QLabel(frmAbout)
        self.lblAbout.setGeometry(QtCore.QRect(10, 10, 391, 41))
        self.lblAbout.setObjectName(_fromUtf8("lblAbout"))

        self.retranslateUi(frmAbout)
        QtCore.QMetaObject.connectSlotsByName(frmAbout)

    def retranslateUi(self, frmAbout):
        frmAbout.setWindowTitle(_translate("frmAbout", "About", None))
        self.lblAbout.setText(_translate("frmAbout", "Program for remember mnemonic tokens. Partially for numbers & dates", None))

