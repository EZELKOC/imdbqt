from PyQt4 import QtCore, QtGui
from kayitoll import Ui_KayitWindow
from main import Ui_AnaWindow
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

class Ui_MainWindow(object):
#######################################################################################################################
    def kayitolWindowShow(self):

        self.kayitolWindow = QtGui.QMainWindow()
        self.ui = Ui_KayitWindow()
        self.ui.setupUi(self.kayitolWindow)
        self.kayitolWindow.show()

    def anaEkranWindowShow(self):
        self.anaEkranWindow = QtGui.QMainWindow()
        self.ui = Ui_AnaWindow()

        self.ui.setupUi(self.anaEkranWindow)
        self.anaEkranWindow.show()

    def loginCheck(self):

        username = self.kullanici_girdisi_user.text()
        parola = self.parola_girdisi_user.text()

        connection = sqlite3.connect("databasess.db")
        sonuc = connection.execute("SELECT * FROM 'Kullanicilar' WHERE Kullanici_Adi = ? AND PAROLA = ?",(username,parola))

        if(len(sonuc.fetchall()) >0 ):
            print ("kullanici bulundu")
            self.anaEkranWindowShow()

        else:
            print("adinizi veya şifrenizi kontrol ediniz")
        connection.close()

    def signUpCheck(self):
         print("tiklandi")
         self.kayitolWindowShow()
#######################################################################################################################
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(895, 764)
        MainWindow.setStyleSheet(_fromUtf8("background-color:rgb(42, 42, 42)"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.imdbtool = QtGui.QToolButton(self.centralwidget)
        self.imdbtool.setGeometry(QtCore.QRect(10, 10, 130, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/imdb.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imdbtool.setIcon(icon)
        self.imdbtool.setIconSize(QtCore.QSize(120, 120))
        self.imdbtool.setObjectName(_fromUtf8("imdbtool"))
        self.kullanici_adi_user = QtGui.QLabel(self.centralwidget)
        self.kullanici_adi_user.setGeometry(QtCore.QRect(260, 220, 111, 41))
        self.kullanici_adi_user.setObjectName(_fromUtf8("kullanici_adi_user"))
        self.parola_user = QtGui.QLabel(self.centralwidget)
        self.parola_user.setGeometry(QtCore.QRect(260, 290, 111, 41))
        self.parola_user.setObjectName(_fromUtf8("parola_user"))
        self.kullanici_girdisi_user = QtGui.QLineEdit(self.centralwidget)
        self.kullanici_girdisi_user.setGeometry(QtCore.QRect(390, 220, 191, 41))
        self.kullanici_girdisi_user.setObjectName(_fromUtf8("kullanici_girdisi_user"))
        self.parola_girdisi_user = QtGui.QLineEdit(self.centralwidget)
        self.parola_girdisi_user.setGeometry(QtCore.QRect(390, 290, 191, 41))
        self.parola_girdisi_user.setObjectName(_fromUtf8("parola_girdisi_user"))
################################################################################################
    #self.parola_girdisi_user.setEchoMode(
#############################################################################################
        self.giris_user_buton = QtGui.QPushButton(self.centralwidget)
        self.giris_user_buton.setGeometry(QtCore.QRect(480, 370, 99, 27))
        self.giris_user_buton.setObjectName(_fromUtf8("giris_user_buton"))
###############################################################################################################
        self.giris_user_buton.clicked.connect(self.loginCheck)
##############################################################################################################
        self.kayitol_user_buton = QtGui.QPushButton(self.centralwidget)
        self.kayitol_user_buton.setGeometry(QtCore.QRect(590, 370, 99, 27))
        self.kayitol_user_buton.setObjectName(_fromUtf8("kayitol_user_buton"))
##############################################################################################################
        self.kayitol_user_buton.clicked.connect(self.signUpCheck)
##############################################################################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.imdbtool.setText(_translate("MainWindow", "...", None))
        self.kullanici_adi_user.setText(_translate("MainWindow", "KULLANICI ADI", None))
        self.parola_user.setText(_translate("MainWindow", "PAROLA", None))
        self.giris_user_buton.setText(_translate("MainWindow", "GIRIS", None))
        self.kayitol_user_buton.setText(_translate("MainWindow", "KAYIT OL", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

