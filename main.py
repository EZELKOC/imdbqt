# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_AnaWindow(object):
    def setupUi(self, AnaWindow):
        AnaWindow.setObjectName(_fromUtf8("AnaWindow"))
        AnaWindow.resize(892, 766)
        AnaWindow.setStyleSheet(_fromUtf8("background-color:rgb(39, 39, 39)"))
        self.centralwidget = QtGui.QWidget(AnaWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 80, 881, 661))
        self.tabWidget.setStyleSheet(_fromUtf8("background-color:rgb(39, 39, 39)"))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../.designer/.designer/İndirilenler/images.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, _fromUtf8(""))
        self.widget = QtGui.QWidget()
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget.addTab(self.widget, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.acilan_icon = QtGui.QFontComboBox(self.tab_4)
        self.acilan_icon.setGeometry(QtCore.QRect(600, 30, 206, 27))
        self.acilan_icon.setObjectName(_fromUtf8("acilan_icon"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.toolButton = QtGui.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(10, 10, 130, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/imdb.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(120, 120))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(640, 20, 211, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        AnaWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(AnaWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        AnaWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AnaWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(AnaWindow)

    def retranslateUi(self, AnaWindow):
        AnaWindow.setWindowTitle(_translate("AnaWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("AnaWindow", "Movie", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("AnaWindow", "TV", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("AnaWindow", "Celebs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("AnaWindow", "New", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("AnaWindow", "Your IMDd", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("AnaWindow", "SETTİNGS", None))
        self.toolButton.setText(_translate("AnaWindow", "...", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AnaWindow = QtGui.QMainWindow()
    ui = Ui_AnaWindow()
    ui.setupUi(AnaWindow)
    AnaWindow.show()
    sys.exit(app.exec_())

