# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transmitter_UI.ui'
#
# Created: Thu Mar 24 21:22:52 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(681, 231)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.BuddyIp = QtGui.QLineEdit(self.centralwidget)
        self.BuddyIp.setObjectName(_fromUtf8("BuddyIp"))
        self.horizontalLayout_3.addWidget(self.BuddyIp)
        self.BuddyName = QtGui.QLineEdit(self.centralwidget)
        self.BuddyName.setObjectName(_fromUtf8("BuddyName"))
        self.horizontalLayout_3.addWidget(self.BuddyName)
        self.VerfiyBuddyButton = QtGui.QPushButton(self.centralwidget)
        self.VerfiyBuddyButton.setObjectName(_fromUtf8("VerfiyBuddyButton"))
        self.horizontalLayout_3.addWidget(self.VerfiyBuddyButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.FileName = QtGui.QLineEdit(self.centralwidget)
        self.FileName.setObjectName(_fromUtf8("FileName"))
        self.horizontalLayout.addWidget(self.FileName)
        self.SelectFile = QtGui.QPushButton(self.centralwidget)
        self.SelectFile.setObjectName(_fromUtf8("SelectFile"))
        self.horizontalLayout.addWidget(self.SelectFile)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.StatusDisplay = QtGui.QTextEdit(self.centralwidget)
        self.StatusDisplay.setObjectName(_fromUtf8("StatusDisplay"))
        self.horizontalLayout_2.addWidget(self.StatusDisplay)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Set User Name", None))
        self.VerfiyBuddyButton.setText(_translate("MainWindow", "Verify", None))
        self.SelectFile.setText(_translate("MainWindow", "Select File ", None))
        self.pushButton_2.setText(_translate("MainWindow", "Send ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

