# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\alex\Documents\Facultate\IOC\help.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_helpWindow(object):
    def setupUi(self, helpWindow):
        helpWindow.setObjectName("helpWindow")
        helpWindow.resize(734, 448)
        self.centralwidget = QtWidgets.QWidget(helpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 20, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 110, 531, 251))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(320, 50, 241, 31))
        self.textBrowser.setObjectName("textBrowser")
        helpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(helpWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 26))
        self.menubar.setObjectName("menubar")
        helpWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(helpWindow)
        self.statusbar.setObjectName("statusbar")
        helpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(helpWindow)
        QtCore.QMetaObject.connectSlotsByName(helpWindow)

    def retranslateUi(self, helpWindow):
        _translate = QtCore.QCoreApplication.translate
        helpWindow.setWindowTitle(_translate("helpWindow", "HELP"))
        self.label_2.setText(_translate("helpWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:9pt;\">Pentru mai multe informatii despre <br/>PyQt5 puteti accesa linkul :</span></p></body></html>"))
        self.label_3.setText(_translate("helpWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Translate App</span></p><p align=\"center\"><br/></p><p><span style=\" font-size:14pt;\">Aceasta aplicatie a fost construită cu scopul de a usura</span></p><p><span style=\" font-size:14pt;\">conversațiile între doi oameni de naționalițăți diferite.</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("helpWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">https://doc.bccnsoft.com/docs/PyQt5/</p></body></html>"))