# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(610, 650)
        Register.setMinimumSize(QtCore.QSize(610, 650))
        Register.setMaximumSize(QtCore.QSize(610, 673))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/beulogo_login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Register.setWindowIcon(icon)
        Register.setStyleSheet("#Register{\n"
"background:url(:/images/images/janko-ferlic-sfL_QOnmy00-unsplash.jpg);\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"background:rgba(0,0,0,0.7);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"\n"
"background:rgba(0,0,0,0.73);\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
"font-size:25px;;\n"
"color:white;\n"
"border:none;\n"
"background:transparent;\n"
"border-bottom:1px solid white;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"background:rgba(0,0,0,0.04);\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"background:rgb(83, 152, 255);\n"
"border-radius:10px;\n"
"color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:none;\n"
"background:rgb(68, 117, 222)\n"
"}\n"
"\n"
"QCheckBox{\n"
"color:silver;\n"
"background:transparent\n"
"}\n"
"QCheckBox:hover{\n"
"color:white;\n"
"}\n"
"\n"
"\n"
"")
        self.frame_2 = QtWidgets.QFrame(Register)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 620, 38))
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_2.setStyleSheet("QFrame{\n"
"background:rgba(0,0,0,0.38);\n"
"}\n"
"QFrame{\n"
"border-radius:none;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"background:rgba(0,0,0,0.40);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_close = QtWidgets.QPushButton(self.frame_2)
        self.btn_close.setGeometry(QtCore.QRect(570, 0, 41, 38))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_close.setFont(font)
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setStyleSheet("QPushButton{\n"
"background:rgba(0, 0, 0,0.15);\n"
"color:silver;\n"
"\n"
"border-radius:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background:red;\n"
"color:white\n"
"}")
        self.btn_close.setObjectName("btn_close")
        self.btn_minimize = QtWidgets.QPushButton(self.frame_2)
        self.btn_minimize.setGeometry(QtCore.QRect(530, 0, 41, 38))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.btn_minimize.setFont(font)
        self.btn_minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimize.setStyleSheet("QPushButton{\n"
"background:rgba(0, 0, 0,0.15);\n"
"border-radius:none;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background:rgba(0, 0, 0,0.6)\n"
"}")
        self.btn_minimize.setObjectName("btn_minimize")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(14, 3, 21, 31))
        self.label_3.setStyleSheet("background:transparent;")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 12, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("\n"
"color:silver;\n"
"background:transparent;")
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(Register)
        self.frame.setGeometry(QtCore.QRect(25, 75, 560, 560))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.name = QtWidgets.QLineEdit(self.frame)
        self.name.setGeometry(QtCore.QRect(20, 145, 250, 61))
        self.name.setText("")
        self.name.setMaxLength(24)
        self.name.setObjectName("name")
        self.baslik = QtWidgets.QLabel(self.frame)
        self.baslik.setGeometry(QtCore.QRect(120, 70, 380, 71))
        self.baslik.setStyleSheet("font-size:40px;\n"
"color:white;\n"
"background:transparent;")
        self.baslik.setObjectName("baslik")
        self.baslik_2 = QtWidgets.QLabel(self.frame)
        self.baslik_2.setGeometry(QtCore.QRect(170, 40, 300, 21))
        self.baslik_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.baslik_2.setStyleSheet("font-size:18px;\n"
"color:white;\n"
"background:transparent;")
        self.baslik_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.baslik_2.setTextFormat(QtCore.Qt.AutoText)
        self.baslik_2.setScaledContents(False)
        self.baslik_2.setOpenExternalLinks(True)
        self.baslik_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.baslik_2.setObjectName("baslik_2")
        self.surname = QtWidgets.QLineEdit(self.frame)
        self.surname.setGeometry(QtCore.QRect(290, 144, 250, 61))
        self.surname.setText("")
        self.surname.setMaxLength(24)
        self.surname.setFrame(True)
        self.surname.setObjectName("surname")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(20, 225, 250, 61))
        self.username.setText("")
        self.username.setMaxLength(24)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(290, 225, 250, 61))
        self.password.setText("")
        self.password.setMaxLength(24)
        self.password.setFrame(True)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.e_mail = QtWidgets.QLineEdit(self.frame)
        self.e_mail.setGeometry(QtCore.QRect(20, 305, 521, 61))
        self.e_mail.setText("")
        self.e_mail.setMaxLength(40)
        self.e_mail.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.e_mail.setObjectName("e_mail")
        self.telefon_no = QtWidgets.QLineEdit(self.frame)
        self.telefon_no.setGeometry(QtCore.QRect(20, 375, 521, 61))
        self.telefon_no.setText("")
        self.telefon_no.setMaxLength(40)
        self.telefon_no.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.telefon_no.setObjectName("telefon_no")
        self.btn_createAccount = QtWidgets.QPushButton(self.frame)
        self.btn_createAccount.setGeometry(QtCore.QRect(90, 474, 400, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_createAccount.setFont(font)
        self.btn_createAccount.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_createAccount.setObjectName("btn_createAccount")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 121))
        self.label.setStyleSheet("background:none;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.baslik.raise_()
        self.name.raise_()
        self.baslik_2.raise_()
        self.surname.raise_()
        self.username.raise_()
        self.password.raise_()
        self.e_mail.raise_()
        self.telefon_no.raise_()
        self.btn_createAccount.raise_()
        self.label.raise_()

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "K??t??phane Sistemi - Kay??t Ol"))
        self.btn_close.setText(_translate("Register", "???"))
        self.btn_minimize.setText(_translate("Register", "_"))
        self.label_3.setText(_translate("Register", "<html><head/><body><p><img src=\":/images/images/beulogo_login.png\" width=\"21\" height=\"30\"/></p></body></html>"))
        self.label_2.setText(_translate("Register", "Kay??t Ol"))
        self.name.setPlaceholderText(_translate("Register", "Ad"))
        self.baslik.setText(_translate("Register", "K??T??PHANE S??STEM??"))
        self.baslik_2.setText(_translate("Register", "B??LENT ECEV??T ??N??VERS??TES??"))
        self.surname.setPlaceholderText(_translate("Register", "Soyad"))
        self.username.setPlaceholderText(_translate("Register", "Kullan??c?? Ad??"))
        self.password.setPlaceholderText(_translate("Register", "??ifre"))
        self.e_mail.setPlaceholderText(_translate("Register", "E-Posta"))
        self.telefon_no.setPlaceholderText(_translate("Register", "Telefon No"))
        self.btn_createAccount.setText(_translate("Register", "Hesap Olu??tur"))
        self.btn_createAccount.setShortcut(_translate("Register", "Return"))
        self.label.setText(_translate("Register", "<html><head/><body><p><img src=\":/images/images/beulogo_login.png\" width=\"67\" height=\"105\"/></p></body></html>"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QDialog()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())
