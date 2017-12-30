# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayitoll.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3

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

class Ui_KayitWindow(object):
    def kayit_olmak(self):
        print ("tiklandi")

        username = self.kul_adi_label_kayit.text()
        email = self.email_label_kayit.text()
        password = self.parola_label_kayit.text()

        connection = sqlite3.connect('/home/loop/imdb/databases.db',timeout=10)
        connection.execute(" INSERT INTO 'Kullanicilar' VALUES(?,?,?)", (username,email,password))
        connection.commit()
        connection.close()
    def setupUi(self, KayitWindow):
        KayitWindow.setObjectName(_fromUtf8("KayitWindow"))
        KayitWindow.resize(894, 767)
        KayitWindow.setStyleSheet(_fromUtf8("background-color:rgb(42, 42, 42)"))
        self.centralwidget = QtGui.QWidget(KayitWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.icontool = QtGui.QToolButton(self.centralwidget)
        self.icontool.setGeometry(QtCore.QRect(10, 0, 130, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/imdb.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icontool.setIcon(icon)
        self.icontool.setIconSize(QtCore.QSize(120, 120))
        self.icontool.setObjectName(_fromUtf8("icontool"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(880, 770, 121, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(880, 810, 121, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(1030, 810, 113, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(930, 610, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(1030, 720, 113, 27))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(1050, 890, 99, 27))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(1030, 760, 113, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(880, 720, 121, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.email_t = QtGui.QLabel(self.centralwidget)
        self.email_t.setGeometry(QtCore.QRect(320, 350, 121, 21))
        self.email_t.setObjectName(_fromUtf8("email_t"))
        self.parola_text = QtGui.QLabel(self.centralwidget)
        self.parola_text.setGeometry(QtCore.QRect(320, 390, 121, 21))
        self.parola_text.setObjectName(_fromUtf8("parola_text"))
        self.parola_label_kayit = QtGui.QLineEdit(self.centralwidget)
        self.parola_label_kayit.setGeometry(QtCore.QRect(470, 390, 113, 27))
        self.parola_label_kayit.setObjectName(_fromUtf8("parola_label_kayit"))
        self.kul_adi_label_kayit = QtGui.QLineEdit(self.centralwidget)
        self.kul_adi_label_kayit.setGeometry(QtCore.QRect(470, 300, 113, 27))
        self.kul_adi_label_kayit.setObjectName(_fromUtf8("kul_adi_label_kayit"))
        self.kayitol_button = QtGui.QPushButton(self.centralwidget)
        self.kayitol_button.setGeometry(QtCore.QRect(490, 470, 99, 27))
        self.kayitol_button.setObjectName(_fromUtf8("kayitol_button"))
        ############################################################################33
        self.kayitol_button.clicked.connect(self.kayit_olmak)
        ###############################################################################
        self.email_label_kayit = QtGui.QLineEdit(self.centralwidget)
        self.email_label_kayit.setGeometry(QtCore.QRect(470, 340, 113, 27))
        self.email_label_kayit.setObjectName(_fromUtf8("email_label_kayit"))
        self.kullanici_adi = QtGui.QLabel(self.centralwidget)
        self.kullanici_adi.setGeometry(QtCore.QRect(320, 300, 121, 21))
        self.kullanici_adi.setObjectName(_fromUtf8("kullanici_adi"))
        KayitWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(KayitWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        KayitWindow.setStatusBar(self.statusbar)

        self.retranslateUi(KayitWindow)
        QtCore.QMetaObject.connectSlotsByName(KayitWindow)

    def retranslateUi(self, KayitWindow):
        KayitWindow.setWindowTitle(_translate("KayitWindow", "MainWindow", None))
        self.icontool.setText(_translate("KayitWindow", "...", None))
        self.label_2.setText(_translate("KayitWindow", "EMAIL", None))
        self.label_3.setText(_translate("KayitWindow", "PAROLA", None))
        self.label_4.setText(_translate("KayitWindow", "HESAP OLUSTUR", None))
        self.pushButton_10.setText(_translate("KayitWindow", "KAYIT OL", None))
        self.label.setText(_translate("KayitWindow", "KULLANICI ADI", None))
        self.email_t.setText(_translate("KayitWindow", "EMAIL", None))
        self.parola_text.setText(_translate("KayitWindow", "PAROLA", None))
        self.kayitol_button.setText(_translate("KayitWindow", "KAYIT OL", None))
        self.kullanici_adi.setText(_translate("KayitWindow", "KULLANICI ADI", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    KayitWindow = QtGui.QMainWindow()
    ui = Ui_KayitWindow()
    ui.setupUi(KayitWindow)
    KayitWindow.show()
    sys.exit(app.exec_())

