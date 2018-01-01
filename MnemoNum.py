# coding: utf-8

import sys
from PyQt4 import QtGui, QtCore
from MnemoForm import Ui_MnemoNum
from db import *
import TestForm
import random
import AboutForm
import MonthForm
import DateForm
import InsDateForm
import TagForm

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

class MonthWindow(QtGui.QMainWindow):
    l = []

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.ui = MonthForm.Ui_Months()
        self.ui.setupUi(self)


        self.populate_table()

        self.ui.tblMonth.cellChanged.connect(self.update_item)


    def update_item(self):
        row = self.ui.tblMonth.currentRow()

        try:
            mnem = self.ui.tblMonth.item(row, 0).text().toUtf8()
            num = row+1
            mnem = mnem.data()
            update_month(str(int(num)), mnem)
        except:
            pass


    def populate_table(self):
        """
            Populate table months
        :return:
        """
        self.l = select_months()    # take months from db
        for i in range(len(self.l)):
            if self.l[i] == None:
                continue
            x = self.l[i]
            x = QtCore.QString(x)
            mon = QtGui.QTableWidgetItem((x))
            mon.setTextAlignment(QtCore.Qt.AlignHCenter)

            self.ui.tblMonth.setItem(i, 0, mon)


class AboutWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.ui = AboutForm.Ui_frmAbout()
        self.ui.setupUi(self)


class TagWindow(QtGui.QMainWindow):
    l = []

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.ui = TagForm.Ui_TagForm()
        self.ui.setupUi(self)
        self.ui.btnAdd.clicked.connect(self.addtag)
        self.select_tags()
        self.ui.tblTags.setColumnWidth(0, 250)
        self.ui.lineEdit.textEdited.connect(self.refresh_table)

    def refresh_table(self):
        tag = self.ui.lineEdit.text().toUtf8().data()
        self.ui.tblTags.clear()
        self.l = select_tag_like(tag)

        self.ui.tblTags.setRowCount(len(self.l))
        n = -1

        for i in range(len(self.l)):
            x = self.l[i]
            x = QtCore.QString(x)
            t = QtGui.QTableWidgetItem(x)
            t.setFlags(QtCore.Qt.ItemIsSelectable)
            self.ui.tblTags.setItem(n, 1, t)
            n += 1

        h0 = QtGui.QTableWidgetItem()
        h0.setText('Tag')
        self.ui.tblTags.setHorizontalHeaderItem(0, h0)


    def addtag(self):
        tag = self.ui.lineEdit.text().toUtf8().data()
        self.ui.tblTags.clear()
        self.l = add_tag(tag)

        h0 = QtGui.QTableWidgetItem()
        h0.setText('Tag')
        self.ui.tblTags.setHorizontalHeaderItem(0, h0)

        self.select_tags()
        self.ui.lineEdit.setText('')


    def select_tags(self):
        self.l = select_tags()

        self.ui.tblTags.setRowCount(len(self.l))
        n = -1

        for i in range(len(self.l)):
            x = self.l[i]
            x = QtCore.QString(x)
            t = QtGui.QTableWidgetItem(x)
            t.setFlags(QtCore.Qt.ItemIsSelectable)
            self.ui.tblTags.setItem(n, 1, t)
            n += 1


class DatesWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.ui = DateForm.Ui_DateWindow()
        self.ui.setupUi(self)

        self.ui.menuAdd.triggered.connect(self.insdate)

    def insdate(self):
        self.ins = InsDateWindow()

        self.ins.show()

class InsDateWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.ui = InsDateForm.Ui_InsDateForm()
        self.ui.setupUi(self)

class TestWindow(QtGui.QMainWindow):
    d = {}
    item = ''
    paintTrigger = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.ui = TestForm.Ui_Form()
        self.ui.setupUi(self)
        self.d = select_mnemo_for_test()
        self.low = ''
        self.high = ''
        # execute test process
        self.exec_test()

        self.ui.eLow.textEdited.connect(self.recount_dict)
        self.ui.eHigh.textEdited.connect(self.recount_dict)
        #self.ui.eHigh.textEdited.connect(self.keyPressEvent)
        self.ui.eAns.textEdited.connect(self.test_next)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_F5:
            self.close()

    def exec_test(self):

        while True:
            n = random.choice(list(self.d))
            try:
                n_cur = int(self.ui.lblAsk.text())
                if len(self.d) > 1:
                    if n != n_cur:
                        self.item = select_mnemo_for_label(n).encode('utf-8')
                        self.ui.lblAsk.setText(str(n))
                        return
                else:
                    self.item = select_mnemo_for_label(n).encode('utf-8')
                    self.ui.lblAsk.setText(str(n))
                    return
            except:
                self.item = select_mnemo_for_label(n).encode('utf-8')
                self.ui.lblAsk.setText(str(n))
                return



    def recount_dict(self):
        d = {}
        try:
            low = int(self.ui.eLow.text().toUtf8().data())
            high = int(self.ui.eHigh.text().toUtf8().data())
            if low > high:                                      # recount if high < low
                t = high
                high = low
                low = t
            self.d = select_mnemo_for_test()                    # if can find both elements then take all dictionary
            for k, v in self.d.items():
                if int(k) >= low and int(k) <= high:
                    d[k] = self.d[k]

            self.d = d
            self.exec_test()
        except:
            pass

    def test_next(self):
        text = self.ui.eAns.text().toUtf8().data()      # str
        if text == self.item:
            self.ui.eAns.setText('')
            self.exec_test()



class MainWindow(QtGui.QMainWindow):
    d = {}

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_MnemoNum()
        self.ui.setupUi(self)
        self.ui.tableWidget.verticalHeader().setVisible(False)
        # self.ui.tableWidget.verticalHeader().setVisible(True)

        # create & populate data
        initialize_db()

        self.populate_table()

        self.ui.tableWidget.cellChanged.connect(self.update_item)
        self.ui.eFilter.textEdited.connect(self.refresh_table)

        self.ui.tableWidget.setColumnWidth(0, 25)
        self.ui.tableWidget.setColumnWidth(1, 245)


        # menu
        self.ui.actionTestNum.triggered.connect(self.TestWin)
        self.ui.actionAbout_Program.triggered.connect(self.AboutWin)
        self.ui.actionMonths_2.triggered.connect(self.MonthWin)
        self.ui.actionDates.triggered.connect(self.DateWin)
        self.ui.actionTags.triggered.connect(self.TagWin)
        self.ui.actionExit_2.triggered.connect(app.exit)

    def MonthWin(self):
        self.month = MonthWindow()
        self.month.show()

    def TestWin(self):
        self.test = TestWindow()

        self.test.show()

    def AboutWin(self):
        self.about = AboutWindow()

        self.about.show()

    def DateWin(self):
        self.dates = DatesWindow()

        self.dates.show()

    def TagWin(self):
        self.dates = TagWindow()

        self.dates.show()

    def update_item(self):
        row = self.ui.tableWidget.currentRow()
        try:
            mnem = self.ui.tableWidget.item(row, 1).text().toUtf8()
            num = self.ui.tableWidget.item(row, 0).text().toUtf8()
            mnem = mnem.data()  # перевод из QByteArray -> QString
            update_mnemo(str(int(num)), mnem)
        except:
            pass

    def take_num(self):
        text = self.ui.eFilter.text().toUtf8().data()
        num = ''
        for i in range(len(text)):
            if text[i].isdigit():
                num = num + text[i]
        return str(int(num))

    def refresh_table(self):
        self.ui.tableWidget.clear()

        h0 = QtGui.QTableWidgetItem()
        h1 = QtGui.QTableWidgetItem()
        h1.setText('Mnemo')

        self.ui.tableWidget.setHorizontalHeaderItem(0, h0)
        self.ui.tableWidget.setHorizontalHeaderItem(1, h1)

        text = self.ui.eFilter.text().toUtf8().data()
        #self.populate_table(text)
        self.select_data(text)
        self.ui.tableWidget.setRowCount(len(self.d))
        n = -1

        if self.ui.eFilter.text().toUtf8().data() == '':
            self.populate_table()

        #self.ui.tableWidget.horizontalHeaderItem(1).setText(_translate("Form", "Mnemo", None))
        l = sorted(list(self.d))

        for i in range(len(l)):
            try:
                #if not int(i)-1 >= 0:
                #    continue
                num = QtGui.QTableWidgetItem(str(int(l[i])))
                num.setFlags(QtCore.Qt.ItemIsSelectable)
                v = self.d[l[i]]
                if v == None:
                    v = ''
                mnem = QtGui.QTableWidgetItem(v)
                mnem.setTextAlignment(QtCore.Qt.AlignHCenter)

                self.ui.tableWidget.setItem(n, 2, num)
                self.ui.tableWidget.setItem(n+1, 1, mnem)
                n += 1
            except:
                pass


        self.update_label()

    def update_lbl(self):
        text = self.ui.eFilter.text().toUtf8().data()
        num = ''
        for i in range(len(text)):
            if text[i] == ' ' or i == len(text)-1:
                lbl = select_mnemo_for_label(num)
                yet_text = self.ui.lblText.text()
                #self.d = select_mnemo_by_num(num)

                num = ''
                try:
                    self.ui.lblText.setText(yet_text + ' ' + lbl)
                except:
                    self.ui.lblText.setText('')
            if text[i].isdigit():
                num = num + text[i]
                self.populate_table_num(num+1)


    def update_label(self):
        try:
            num = self.take_num()
            text = select_mnemo_for_label(num)
            try:
                self.ui.lblText.setText(text)
            except:
                self.ui.lblText.setText('')
        except:
            self.ui.lblText.setText('')

    def test(self):
        try:

            row = self.ui.tableWidget.currentRow()

            mnem = self.ui.tableWidget.item(row, 0).text()
            num = self.ui.tableWidget.item(row, 1).text()

            update_mnemo(num, mnem)
        except:
            pass


    def populate_table(self, mnemo=None):
        self.select_data(mnemo)
        self.ui.tableWidget.setRowCount(len(self.d))
        n = -1
        for k, v in self.d.items():
            if not int(k) >= 0:
                continue
            num = QtGui.QTableWidgetItem(str(k+1))
            num.setFlags(QtCore.Qt.ItemIsSelectable)
            if v == None:
                v = ''
            mnem = QtGui.QTableWidgetItem(v)
            mnem.setTextAlignment(QtCore.Qt.AlignHCenter)

            self.ui.tableWidget.setItem(n, 2, num)
            self.ui.tableWidget.setItem(n, 1, mnem)
            n += 1

    def populate_table_num(self, num=None):
        self.d = select_mnemo_by_num(num)
        self.ui.tableWidget.setRowCount(len(self.d))
        n = -1
        for k, v in self.d.items():
            if not int(k) >= 0:
                continue
            num = QtGui.QTableWidgetItem(str(k+1))
            num.setFlags(QtCore.Qt.ItemIsSelectable)
            if v == None:
                v = ''
            mnem = QtGui.QTableWidgetItem(v)
            mnem.setTextAlignment(QtCore.Qt.AlignHCenter)


            self.ui.tableWidget.setItem(n, 2, num)
            self.ui.tableWidget.setItem(n, 1, mnem)
            n += 1

    def select_data(self, mnemo=None):
        self.d = select_mnemo(mnemo)





if __name__ == '__main__':
    db_name = os.getcwd() + '\MnemoNum.db'
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


