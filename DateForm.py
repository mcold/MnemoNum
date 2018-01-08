# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DateForm.ui'
#
# Created: Sun Dec 31 16:27:19 2017
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

class Ui_DateWindow(object):
    def setupUi(self, DateWindow):
        DateWindow.setObjectName(_fromUtf8("DateWindow"))
        DateWindow.resize(671, 600)
        self.centralwidget = QtGui.QWidget(DateWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tblDates = QtGui.QTableWidget(self.centralwidget)
        self.tblDates.setGeometry(QtCore.QRect(10, 100, 651, 451))
        self.tblDates.setObjectName(_fromUtf8("tblDates"))
        self.tblDates.setColumnCount(5)
        self.tblDates.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblDates.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblDates.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblDates.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblDates.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tblDates.setHorizontalHeaderItem(4, item)
        self.cmbTag = QtGui.QComboBox(self.centralwidget)
        self.cmbTag.setGeometry(QtCore.QRect(340, 30, 321, 22))
        self.cmbTag.setObjectName(_fromUtf8("cmbTag"))
        self.eFrom = QtGui.QLineEdit(self.centralwidget)
        self.eFrom.setGeometry(QtCore.QRect(10, 30, 131, 20))
        self.eFrom.setAlignment(QtCore.Qt.AlignCenter)
        self.eFrom.setObjectName(_fromUtf8("eFrom"))
        self.eTo = QtGui.QLineEdit(self.centralwidget)
        self.eTo.setGeometry(QtCore.QRect(180, 30, 141, 20))
        self.eTo.setAlignment(QtCore.Qt.AlignCenter)
        self.eTo.setObjectName(_fromUtf8("eTo"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1410, 130, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.eEvent = QtGui.QLineEdit(self.centralwidget)
        self.eEvent.setGeometry(QtCore.QRect(10, 60, 651, 20))
        self.eEvent.setObjectName(_fromUtf8("eEvent"))
        DateWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(DateWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTest = QtGui.QMenu(self.menubar)
        self.menuTest.setObjectName(_fromUtf8("menuTest"))
        self.menuAdd = QtGui.QMenu(self.menubar)
        self.menuAdd.setObjectName(_fromUtf8("menuAdd"))
        DateWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(DateWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        DateWindow.setStatusBar(self.statusbar)
        self.actionTest_Dates = QtGui.QAction(DateWindow)
        self.actionTest_Dates.setObjectName(_fromUtf8("actionTest_Dates"))
        self.actionTag = QtGui.QAction(DateWindow)
        self.actionTag.setObjectName(_fromUtf8("actionTag"))
        self.actionDate = QtGui.QAction(DateWindow)
        self.actionDate.setObjectName(_fromUtf8("actionDate"))
        self.menuTest.addAction(self.actionTest_Dates)
        self.menuAdd.addAction(self.actionTag)
        self.menuAdd.addAction(self.actionDate)
        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menuAdd.menuAction())

        self.retranslateUi(DateWindow)
        QtCore.QMetaObject.connectSlotsByName(DateWindow)

    def retranslateUi(self, DateWindow):
        DateWindow.setWindowTitle(_translate("DateWindow", "Dates", None))
        item = self.tblDates.horizontalHeaderItem(0)
        item.setText(_translate("DateWindow", "Event", None))
        item = self.tblDates.horizontalHeaderItem(1)
        item.setText(_translate("DateWindow", "Day", None))
        item = self.tblDates.horizontalHeaderItem(2)
        item.setText(_translate("DateWindow", "Month", None))
        item = self.tblDates.horizontalHeaderItem(3)
        item.setText(_translate("DateWindow", "Year", None))
        item = self.tblDates.horizontalHeaderItem(4)
        item.setText(_translate("DateWindow", "Tag", None))
        self.menuTest.setTitle(_translate("DateWindow", "Exercise", None))
        self.menuAdd.setTitle(_translate("DateWindow", "Add", None))
        self.actionTest_Dates.setText(_translate("DateWindow", "Test Dates", None))
        self.actionTag.setText(_translate("DateWindow", "Tag", None))
        self.actionDate.setText(_translate("DateWindow", "Date", None))

