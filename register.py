import time
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import QPoint
import sys

from warning import warning
from sqlExecute import sqlExecute
from ui_tasarim.Ui_register import Ui_Register

class register(QDialog, Ui_Register):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.oldPos = self.pos()
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_createAccount.clicked.connect(self.createAccount)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.db_data = {}
        self.error_msg = []
        self.login = True

    def createAccount(self):
        self.db_data = {
            'ad': self.name.text(),
            'soyad': self.surname.text(),
            'kullanici_adi': self.username.text(),
            'parola': self.password.text(),
            'e_mail': self.e_mail.text(),
            'telefon_no': self.telefon_no.text()
        }
        # ------------------ Hata Kontrolü Başlangıç ------------------
        if (warning("Lütfen Boş Alanları Doldurunuz").exec_() if [self.db_data[i] for i in self.db_data].count('') > 0 else False) is not False:
            return

        self.error_msg = "Ad ve Soyad Alanını En Az 2 Karakter Olmalıdır"
        if (warning(self.error_msg).exec_() if len(self.db_data['ad']) < 2 or len(self.db_data['soyad']) < 2 else False) is not False:
            return

        self.error_msg = "Kullanıcı Adı En Az Altı Karakter Olmalıdır"
        if (warning(self.error_msg).exec_() if len(self.db_data['kullanici_adi']) < 6 else False) is not False:
            return

        self.error_msg = "Lütfen Geçerli Bir E-Posta Adresi Giriniz"
        if (warning(self.error_msg).exec_() if self.db_data['e_mail'].count('@') == 0 or self.db_data['e_mail'].count('.com') == 0 else False) is not False:
            return

        self.error_msg = "Lütfen Şifrenizde Büyük-Küçük Harf ve Rakam Kullanınız"
        if (warning(self.error_msg).exec_() if ([i.isupper() for i in self.db_data['parola']].count(True) < 1 or [i.islower() for i in self.db_data['parola']].count(True) < 1 or [i.isalpha() for i in self.db_data['parola']].count(False) < 1) else False) is not False:
            return
        # ------------------ Hata Kontrolü Bitiş ------------------
        
        # Kayıt İşlemi
        sql = sqlExecute(self.username.text(), self.password.text())
        sql.register(self.db_data)
        time.sleep(0.8)
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = register()
    win.show()
    sys.exit(app.exec())
