# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MnemoForm.ui'
#
# Created: Sun Dec 31 14:38:06 2017
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

class Ui_MnemoNum(object):
    def setupUi(self, MnemoNum):
        MnemoNum.setObjectName(_fromUtf8("MnemoNum"))
        MnemoNum.resize(309, 373)
        self.centralwidget = QtGui.QWidget(MnemoNum)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 90, 291, 241))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.lblText = QtGui.QLabel(self.centralwidget)
        self.lblText.setGeometry(QtCore.QRect(10, 60, 291, 16))
        self.lblText.setText(_fromUtf8(""))
        self.lblText.setAlignment(QtCore.Qt.AlignCenter)
        self.lblText.setObjectName(_fromUtf8("lblText"))
        self.eFilter = QtGui.QLineEdit(self.centralwidget)
        self.eFilter.setGeometry(QtCore.QRect(10, 30, 291, 20))
        self.eFilter.setAlignment(QtCore.Qt.AlignCenter)
        self.eFilter.setObjectName(_fromUtf8("eFilter"))
        MnemoNum.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MnemoNum)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 309, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuDB = QtGui.QMenu(self.menubar)
        self.menuDB.setObjectName(_fromUtf8("menuDB"))
        self.menuExercise = QtGui.QMenu(self.menubar)
        self.menuExercise.setObjectName(_fromUtf8("menuExercise"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuAddiction = QtGui.QMenu(self.menubar)
        self.menuAddiction.setObjectName(_fromUtf8("menuAddiction"))
        MnemoNum.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MnemoNum)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MnemoNum.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MnemoNum)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExport = QtGui.QAction(MnemoNum)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionImport = QtGui.QAction(MnemoNum)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionExit_2 = QtGui.QAction(MnemoNum)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))
        self.actionTestNum = QtGui.QAction(MnemoNum)
        self.actionTestNum.setObjectName(_fromUtf8("actionTestNum"))
        self.actionAbout_Program = QtGui.QAction(MnemoNum)
        self.actionAbout_Program.setObjectName(_fromUtf8("actionAbout_Program"))
        self.actionMonths = QtGui.QAction(MnemoNum)
        self.actionMonths.setObjectName(_fromUtf8("actionMonths"))
        self.actionMonths_2 = QtGui.QAction(MnemoNum)
        self.actionMonths_2.setObjectName(_fromUtf8("actionMonths_2"))
        self.actionDates = QtGui.QAction(MnemoNum)
        self.actionDates.setObjectName(_fromUtf8("actionDates"))
        self.actionTags = QtGui.QAction(MnemoNum)
        self.actionTags.setObjectName(_fromUtf8("actionTags"))
        self.menuDB.addAction(self.actionExport)
        self.menuDB.addAction(self.actionImport)
        self.menuDB.addSeparator()
        self.menuDB.addAction(self.actionExit_2)
        self.menuExercise.addAction(self.actionTestNum)
        self.menuAbout.addAction(self.actionAbout_Program)
        self.menuAddiction.addAction(self.actionMonths_2)
        self.menuAddiction.addAction(self.actionDates)
        self.menuAddiction.addAction(self.actionTags)
        self.menubar.addAction(self.menuDB.menuAction())
        self.menubar.addAction(self.menuExercise.menuAction())
        self.menubar.addAction(self.menuAddiction.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MnemoNum)
        QtCore.QMetaObject.connectSlotsByName(MnemoNum)

    def retranslateUi(self, MnemoNum):
        MnemoNum.setWindowTitle(_translate("MnemoNum", "MnemoWindow", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MnemoNum", "Mnemo", None))
        self.menuDB.setTitle(_translate("MnemoNum", "DB", None))
        self.menuExercise.setTitle(_translate("MnemoNum", "Exercise", None))
        self.menuAbout.setTitle(_translate("MnemoNum", "About", None))
        self.menuAddiction.setTitle(_translate("MnemoNum", "Addiction", None))
        self.actionExit.setText(_translate("MnemoNum", "Exit", None))
        self.actionExport.setText(_translate("MnemoNum", "Export", None))
        self.actionImport.setText(_translate("MnemoNum", "Import", None))
        self.actionExit_2.setText(_translate("MnemoNum", "Exit", None))
        self.actionTestNum.setText(_translate("MnemoNum", "Numbers", None))
        self.actionAbout_Program.setText(_translate("MnemoNum", "About Program", None))
        self.actionMonths.setText(_translate("MnemoNum", "Months", None))
        self.actionMonths_2.setText(_translate("MnemoNum", "Months", None))
        self.actionDates.setText(_translate("MnemoNum", "Dates", None))
        self.actionTags.setText(_translate("MnemoNum", "Tags", None))

