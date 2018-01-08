# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TagForm.ui'
#
# Created: Tue Jan 02 11:21:18 2018
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

class Ui_TagForm(object):
    def setupUi(self, TagForm):
        TagForm.setObjectName(_fromUtf8("TagForm"))
        TagForm.resize(341, 414)
        self.lineEdit = QtGui.QLineEdit(TagForm)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 241, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.tblTags = QtGui.QTableWidget(TagForm)
        self.tblTags.setGeometry(QtCore.QRect(10, 50, 321, 351))
        self.tblTags.setObjectName(_fromUtf8("tblTags"))
        self.tblTags.setColumnCount(1)
        self.tblTags.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblTags.setHorizontalHeaderItem(0, item)
        self.btnAdd = QtGui.QPushButton(TagForm)
        self.btnAdd.setGeometry(QtCore.QRect(260, 10, 75, 23))
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))

        self.retranslateUi(TagForm)
        QtCore.QMetaObject.connectSlotsByName(TagForm)

    def retranslateUi(self, TagForm):
        TagForm.setWindowTitle(_translate("TagForm", "Tags", None))
        item = self.tblTags.horizontalHeaderItem(0)
        item.setText(_translate("TagForm", "Tag", None))
        self.btnAdd.setText(_translate("TagForm", "Add", None))

