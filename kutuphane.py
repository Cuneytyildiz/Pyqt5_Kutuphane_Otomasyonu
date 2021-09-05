from re import A

from PyQt5 import QtWidgets
from login import logIn
from warning import warning
from sqlExecute import sqlExecute
from ui_tasarim.Ui_kutuphane import Ui_MainWindow


import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import *

class kutuphane(QMainWindow, Ui_MainWindow):
    def __init__(self):
        login = logIn()
        login.exec_()
        super().__init__()
        self.setupUi(self)
        self.oldPos = self.pos()
        # Personel Bilgisi
        self.username = login.username.text()
        self.password = login.password.text()
        self.userInfo = {}
        # Menü ve tool bar
        self.btn_close.clicked.connect(self.close)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Giriş
        if login.giris_control is None:
            sys.exit()
        else:
            # Sol Menü
            self.menuStack.hide()
            self.btn_profil.clicked.connect(self.showWidget)
            self.btn_kitap.clicked.connect(self.showWidget)
            self.btn_odunc.clicked.connect(self.showWidget)
            self.btn_kullanici.clicked.connect(self.showWidget)
            self.btn_kitap_kayit.clicked.connect(self.showWidget)
            self.btn_kitap_duzenle.clicked.connect(self.showWidget)
            self.btn_kitap_test.clicked.connect(self.showWidget)
            self.btn_odunc_ver.clicked.connect(self.showWidget)
            self.btn_odunc_iade.clicked.connect(self.showWidget)
            self.btn_odunc_test.clicked.connect(self.showWidget)
            self.btn_kullanici_kayit.clicked.connect(self.showWidget)
            self.btn_kullanici_liste.clicked.connect(self.showWidget)
            self.open_close_control = "close"
            self.last_menu = ["profil"]
            self.opened_menu = [self.btn_profil]

            # Veritabanı bağlantısı ve Widgettaki verilerin Güncellenmesi
            self.connectDatabase()
            self.setInfo()

            ##### Ana İşlem Butonları ####
            # Profil Kısmı
            self.btn_profilParola.clicked.connect(self.profilSection)
            # Kitap Kısmı
            self.combo_edit_kitap.activated.connect(self.kitapSection)
            self.btn_kitapEkle.clicked.connect(self.kitapSection)
            self.btn_kitapDuzenle.clicked.connect(self.kitapSection)
            self.btn_kitapSil.clicked.connect(self.kitapSection)
            self.btn_kitapBilgileriGetir.clicked.connect(self.kitapSection)
            self.btn_kitapBilgileriGetir_2.clicked.connect(self.kitapSection)
            self.btn_kullaniciAra_2.clicked.connect(self.kitapSection)
            # Ödünç Kısmı
            self.btn_oduncVer.clicked.connect(self.oduncSection)
            self.btn_oduncIade.clicked.connect(self.oduncSection)
            self.combo_odunc_kitap.activated.connect(self.oduncSection)
            self.combo_odunc_kullanici.activated.connect(self.oduncSection)
            self.combo_odunc_bilgi.activated.connect(self.oduncSection)
            self.btn_oduncAra.clicked.connect(self.oduncSection)
            self.btn_oduncListesiGetir.clicked.connect(self.oduncSection)
            # Kullanıcı Kısmı
            self.btn_kullaniciKayit.clicked.connect(self.kullaniciSection)
            self.btn_kullaniciAra.clicked.connect(self.kullaniciSection)
            self.btn_kullaniciBilgileriGetir.clicked.connect(
                self.kullaniciSection)

    def connectDatabase(self):
        self.sql = sqlExecute(self.username, self.password)
        self.sql.config['database'] = '%s' % (self.username)
        info = self.sql.personelBilgi()
        self.userInfo = {
            'ad': info[0]['ad'],
            'soyad': info[0]['soyad'],
            'e_mail': info[0]['e_mail'],
            'telefon_no': info[0]['telefon_no'],
        }

    def setInfo(self):
        self.kitap_duzenle_show_hide = [self.kitap_edit_ad, self.kitap_edit_yazar, self.kitap_edit_yayinevi,
                                        self.kitap_edit_tur, self.kitap_edit_sayfa, self.kitap_edit_basim]

        self.odunc_ver_kitap_show_hide = [self.odunc_ver_barkod, self.odunc_ver_kitap, self.odunc_ver_yazar,
                                          self.odunc_ver_yayinevi]

        self.odunc_ver_kullanici_show_hide = [
            self.odunc_ver_ogrno, self.odunc_ver_adsoyad, self.odunc_ver_telefon, self.odunc_ver_tarih]

        self.odunc_iade_show_hide = [
            self.odunc_iade_barkod, self.odunc_iade_kitap, self.odunc_iade_yazar, self.odunc_iade_yayinevi, self.odunc_iade_ogrno, 
            self.odunc_iade_adsoyad, self.odunc_iade_telefon, self.odunc_iade_tarih]

        # kitap düzenle bölümü güncelleme
        def kitapCombo():
            kitapData = self.sql.kitapBilgi()
            self.combo_edit_kitap.clear()
            self.combo_edit_kitap.addItems(kitapData['kitapbilgi'])
            [i.hide for i in self.kitap_duzenle_show_hide]

        # ödünç verme bölümü güncelleme
        def oduncCombo():
            oduncData = self.sql.oduncBilgi()
            self.combo_odunc_kitap.clear()
            self.combo_odunc_kitap.addItems(oduncData['kitapbilgi'])
            [i.hide for i in self.odunc_ver_kitap_show_hide]

        # ödünç verme bölümü kullanıcı bilgisi güncelleme
        def kullaniciCombo():
            kullaniciData = self.sql.kullaniciBilgi()
            self.combo_odunc_kullanici.clear()
            self.combo_odunc_kullanici.addItems(
                kullaniciData['kullanicibilgi'])
            [i.hide for i in self.odunc_ver_kullanici_show_hide]
        # iade bölümü kullanıcı bilgisi güncelleme
        def iadeCombo():
            kullaniciData = self.sql.iadeBilgi()
            self.combo_odunc_bilgi.clear()
            self.combo_odunc_bilgi.addItems(
                kullaniciData['iadebilgi'])
            [i.hide for i in self.odunc_iade_show_hide]
        # Personel profil bilgisi getirilmesi
        def profilBilgisi():
            personelBilgi = self.sql.profilBilgi()[0]
            lineEdits = [self.profil_ad, self.profil_soyad, self.profil_kullanici_adi,
                         self.profil_parola, self.profil_mail, self.profil_telefon]
            print(personelBilgi)
            Info = [personelBilgi['kullanici_adi'], personelBilgi['parola'], personelBilgi['ad'],
                    personelBilgi['soyad'], personelBilgi['e_mail'], personelBilgi['telefon_no']]
            [a.setText(str(b)) for a, b in zip(lineEdits, Info)]

        kitapCombo()
        oduncCombo()
        kullaniciCombo()
        iadeCombo()
        profilBilgisi()

        self.label_username.setText("@"+self.username)
        self.label_telefon_no.setText(self.userInfo['telefon_no'])

    def profilSection(self):

        def yeniParola():
            yeni = self.profil_parola_yeni.text()
            self.sql.parolaDegistir(yeni)

        sender = self.sender()
        if str(sender.objectName()) == "btn_profilParola":
            yeniParola()
            self.setInfo()
            warning('Parola Değiştirme İşlemi Başarılı').exec_()
            self.profil_parola_yeni.clear()
        
    def kitapSection(self):

        def kitapEkle():
            kitapData = {
                'kitap_adi': self.kitap_ekle_adi.text(),
                'yazar_adi': self.kitap_ekle_yazar.text(),
                'yayinevi': self.kitap_ekle_yayinevi.text(),
                'tur': self.kitap_ekle_tur.text(),
                'sayfa': self.kitap_ekle_sayfa.text(),
                'basim': self.kitap_ekle_basim.text(),
            }

            if (warning("Lütfen Boş Alanları Doldurunuz").exec_() if [i for i in kitapData.values()].count('') > 0 else False) is not False:
                return
            self.sql.kitapEkle(kitapData)

            [i.clear() for i in [self.kitap_ekle_adi, self.kitap_ekle_yazar, self.kitap_ekle_yayinevi, self.kitap_ekle_tur,
                                 self.kitap_ekle_sayfa, self.kitap_ekle_basim]]

            warning('Kitap Ekleme İşlemi Başarılı').exec_()
            self.setInfo()

        def bilgileriGetir():
            if self.combo_edit_kitap.currentText() != "":
                kitapAdi = self.combo_edit_kitap.currentText().split(
                    " ")[0]
                thelearnerInfo = (
                    self.sql.KitapInfo(kitapAdi))[0]
                lineEdits = [self.kitap_edit_ad, self.kitap_edit_yazar, self.kitap_edit_yayinevi,
                             self.kitap_edit_tur, self.kitap_edit_sayfa, self.kitap_edit_basim]
                Info = [thelearnerInfo['kitap_adi'], thelearnerInfo['yazar_adi'], thelearnerInfo['yayinevi'],
                        thelearnerInfo['tur'], thelearnerInfo['sayfa'], thelearnerInfo['basim']]
                [a.setText(str(b)) for a, b in zip(lineEdits, Info)]

        def KitapGuncelle():
            kitapData = {
                # 'kitap_adi': self.kitap_edit_ad.text(),
                'yazar_adi': self.kitap_edit_yazar.text(),
                'yayinevi': self.kitap_edit_yayinevi.text(),
                'tur': self.kitap_edit_tur.text(),
                'sayfa': self.kitap_edit_sayfa.text(),
                'basim': self.kitap_edit_basim.text(),
                'kitap_adi': self.kitap_edit_ad.text(),
            }
            if (warning("Lütfen Boş Alanları Doldurunuz").exec_() if [i for i in kitapData.values()].count(
                    '') > 0 else False) is not False:
                return
            kitapData['kitap_adi'] = self.combo_edit_kitap.currentText().split(
                " ")[0]

            self.sql.kitapGuncelle(kitapData)
            warning('Kitap Güncelleme İşlemi Başarılı').exec_()

            [i.clear() for i in [self.kitap_edit_ad, self.kitap_edit_basim, self.kitap_edit_sayfa, self.kitap_edit_tur,
                                 self.kitap_edit_yayinevi, self.kitap_edit_yazar]]

            self.setInfo()

        def kitap_sil():
            kitapadi = self.combo_edit_kitap.currentText().split(
                " ")[0]
            # delete
            self.sql.KitapSil(kitapadi)
            # Hide the QLineEdits fields
            warning('Kitap Silme İşlemi Başarılı').exec_()

            # clear the QLineEdit Fields
            [i.clear() for i in [self.kitap_edit_ad, self.kitap_edit_basim, self.kitap_edit_sayfa, self.kitap_edit_tur,
                                 self.kitap_edit_yayinevi, self.kitap_edit_yazar]]
            # for update widgets
            self.setInfo()

        def kitap_liste():
            liste = self.sql.KitapListe()
            while self.tableWidget.rowCount() > 0:
                self.tableWidget.removeRow(0)
            # self.tableWidget.setRowcount(0)
            for row_number, row_data in enumerate(liste):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(
                        row_number, column_number, QtWidgets.QTableWidgetItem(str(row_data[data])))

        def kitap_ara():
            while self.tableWidget.rowCount() > 0:
                self.tableWidget.removeRow(0)

            kitapAdi = self.kullanici_ogr_no_3.text()
            aranan_kitap = self.sql.KitapInfo(kitapAdi)
            if aranan_kitap == []:
                warning('Aranan Kitap Bulunamadı').exec_()
            else:
                for row_number, row_data in enumerate(aranan_kitap):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(
                            row_number, column_number, QtWidgets.QTableWidgetItem(str(row_data[data])))

                [i.clear() for i in [self.kullanici_ogr_no_3]]

        sender = self.sender()
        if str(sender.objectName()) == "combo_edit_kitap":
            bilgileriGetir()
        elif sender.text() == "Kitap Ekle":
            kitapEkle()
        elif sender.text() == "BİLGİLERİ GETİR":
            bilgileriGetir()
        elif sender.text() == "Kitap Düzenle":
            warning('Lütfen öncelikle herhangi bir kitap bilgisi getirin').exec_(
            ) if self.kitap_edit_ad.isHidden() else KitapGuncelle()
        elif sender.text() == "Kitap Sil":
            warning('Lütfen öncelikle herhangi bir öğrenci bilgisi getirin').exec_(
            ) if self.kitap_edit_ad.isHidden() else kitap_sil()
        elif sender.text() == "Kitap Bilgisi":
            warning('Lütfen öncelikle herhangi bir öğrenci bilgisi getirin').exec_(
            ) if self.kullanici_ogr_no_3.isHidden() else kitap_liste()
        elif sender.text() == "Ara":
            warning('Lütfen öncelikle herhangi bir öğrenci bilgisi getirin').exec_(
            ) if self.kullanici_ogr_no_3.isHidden() else kitap_ara()

    def oduncSection(self):

        def oduncVer():
            oduncData = {
                'kitap_id': self.odunc_ver_barkod.text(),
                'kitap_adi': self.odunc_ver_kitap.text(),
                'yazar_adi': self.odunc_ver_yazar.text(),
                'yayinevi': self.odunc_ver_yayinevi.text(),
                'ogr_no': self.odunc_ver_ogrno.text(),
                'ad_soyad': self.odunc_ver_adsoyad.text(),
                'telefon': self.odunc_ver_telefon.text(),
                'alinma_tarih': self.odunc_ver_tarih.text(),
            }
            # is there any empyt field
            if (warning("Lütfen Boş Alanları Doldurunuz").exec_() if [i for i in oduncData.values()].count('') > 0 else False) is not False:
                return
            # adding new learner
            kitapId = self.odunc_ver_barkod.text()
            self.sql.oduncEkle(oduncData, kitapId)

            [i.clear() for i in [self.odunc_ver_barkod, self.odunc_ver_kitap, self.odunc_ver_yazar, self.odunc_ver_yayinevi,
                                 self.odunc_ver_ogrno, self.odunc_ver_adsoyad, self.odunc_ver_telefon, self.odunc_ver_tarih]]

            warning('Ödünç Verme İşlemi Başarılı').exec_()

            [i.clear() for i in [self.odunc_ver_barkod, self.odunc_ver_kitap, self.odunc_ver_yazar, self.odunc_ver_yayinevi,
                               self.odunc_ver_ogrno, self.odunc_ver_adsoyad, self.odunc_ver_telefon, self.odunc_ver_tarih]]
            self.setInfo()

        def oduncKitapGetir():
            if self.combo_odunc_kitap.currentText() != "":
                kitapId = self.combo_odunc_kitap.currentText().split(
                    " ")[0]
                oduncInfo = (
                    self.sql.oduncInfo(kitapId))[0]
                lineEdits = [self.odunc_ver_barkod, self.odunc_ver_kitap, self.odunc_ver_yazar,
                             self.odunc_ver_yayinevi]
                Info = [oduncInfo['kitap_id'], oduncInfo['kitap_adi'], oduncInfo['yazar_adi'],
                        oduncInfo['yayinevi']]
                [a.setText(str(b)) for a, b in zip(lineEdits, Info)]

        def oduncKullaniciGetir():
            if self.combo_odunc_kullanici.currentText() != "":
                ogrNo = self.combo_odunc_kullanici.currentText().split(
                    " ")[0]
                oduncInfo = (
                    self.sql.KullaniciInfo(ogrNo))[0]
                lineEdits = [self.odunc_ver_ogrno,
                             self.odunc_ver_adsoyad, self.odunc_ver_telefon]
                Info = [oduncInfo['ogrenci_no'],
                        oduncInfo['ad']+" "+oduncInfo['soyad'], oduncInfo['telefon_no']]
                [a.setText(str(b)) for a, b in zip(lineEdits, Info)]

        def iadeBilgiGetir():
            if self.combo_odunc_bilgi.currentText() != "":
                oduncId = self.combo_odunc_bilgi.currentText().split(
                    " ")[0]
                oduncInfo = (
                    self.sql.iadeInfo(oduncId))[0]
                lineEdits = [self.odunc_iade_barkod, self.odunc_iade_kitap, self.odunc_iade_yazar,
                             self.odunc_iade_yayinevi, self.odunc_iade_ogrno, self.odunc_iade_adsoyad, self.odunc_iade_telefon]
                Info = [oduncInfo['kitap_id'], oduncInfo['kitap_adi'], oduncInfo['yazar_adi'],
                        oduncInfo['yayinevi'], oduncInfo['ogr_no'], oduncInfo['ad_soyad'], oduncInfo['telefon']]
                [a.setText(str(b)) for a, b in zip(lineEdits, Info)]

        def oduncİade():
            oduncId = self.combo_odunc_bilgi.currentText().split(
                " ")[0]

            oduncData = {
                'kitap_id': self.odunc_iade_barkod.text(),
                'teslim_tarihi': self.odunc_iade_tarih.text(),
            }
            if (warning("Lütfen Boş Alanları Doldurunuz").exec_() if [i for i in oduncData.values()].count(
                    '') > 0 else False) is not False:
                return

            oduncData['iadebilgi'] = self.combo_odunc_bilgi.currentText().split(
                " ")[0]

            self.sql.iadeEkle(oduncData, oduncId)
            warning('Ödünç İade İşlemi Başarılı').exec_()

            [i.clear() for i in [self.odunc_iade_barkod, self.odunc_iade_kitap, self.odunc_iade_yazar, self.odunc_iade_yayinevi,
                                 self.odunc_iade_ogrno, self.odunc_iade_adsoyad, self.odunc_iade_telefon, self.odunc_iade_tarih]]
            self.setInfo()

        def odunc_liste():
            liste = self.sql.oduncListe()
            while self.tableWidget_2.rowCount() > 0:
                self.tableWidget_2.removeRow(0)
            # self.tableWidget.setRowcount(0)
            for row_number, row_data in enumerate(liste):
                self.tableWidget_2.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_2.setItem(
                        row_number, column_number, QtWidgets.QTableWidgetItem(str(row_data[data])))

        def odunc_ara():
            while self.tableWidget_2.rowCount() > 0:
                self.tableWidget_2.removeRow(0)

            ogrNo = self.kullanici_ogr_no_4.text()
            aranan_islem = self.sql.iadeAra(ogrNo)
            if aranan_islem == []:
                warning('Aranan Öğrenicye Ait İşlem Bulunamadı').exec_()
            else:
                for row_number, row_data in enumerate(aranan_islem):
                    self.tableWidget_2.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget_2.setItem(
                            row_number, column_number, QtWidgets.QTableWidgetItem(str(row_data[data])))
                [i.clear() for i in [self.kullanici_ogr_no_4]]

        sender = self.sender()
        if str(sender.objectName()) == "combo_odunc_kitap":
            oduncKitapGetir()
        elif str(sender.objectName()) == "combo_odunc_kullanici":
            oduncKullaniciGetir()
        elif str(sender.objectName()) == "combo_odunc_bilgi":
            iadeBilgiGetir()
        elif sender.text() == "KİTAP BİLGİSİ":
            oduncKitapGetir()
        elif sender.text() == "KULLANICI BİLGİSİ":
            oduncKullaniciGetir()
        elif sender.text() == "Ödünç Ver":
            oduncVer()
        elif sender.text() == "Kitap İade":
            oduncİade()
        elif sender.text() == "Ara":
            odunc_ara()
        elif sender.text() == "Ödünç Listesi":
            odunc_liste()

    def kullaniciSection(self):

        def kullaniciEkle():
            kullaniciData = {
                'ogrenci_no': self.kullanici_ogr_no.text(),
                'ad': self.kullanici_adi.text(),
                'soyad': self.kullanici_soyad.text(),
                'telefon_no': self.kullanici_telefon_no.text(),
                'e_mail': self.kullanici_mail.text(),
            }
            if (warning("Lütfen Boş Alanları Doldurunuz").exec_() if [i for i in kullaniciData.values()].count('') > 0 else False) is not False:
                return

            self.sql.KullaniciEkle(kullaniciData)

            [i.clear() for i in [self.kullanici_ogr_no, self.kullanici_adi, self.kullanici_soyad, self.kullanici_telefon_no,
                                 self.kullanici_mail]]

            warning('Kullanıcı Ekleme İşlemi Başarılı').exec_()
            self.setInfo()

        def kullanici_liste():
            liste = self.sql.KullaniciListe()
            while self.tableWidget_4.rowCount() > 0:
                self.tableWidget_4.removeRow(0)
            # self.tableWidget.setRowcount(0)
            for row_number, row_data in enumerate(liste):
                self.tableWidget_4.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget_4.setItem(
                        row_number, column_number, QtWidgets.QTableWidgetItem(str(row_data[data])))

        def kullanici_ara():
            while self.tableWidget_4.rowCount() > 0:
                self.tableWidget_4.removeRow(0)

            ogrNo = self.kullanici_ogr_no_2.text()
            aranan_kullanici = self.sql.KullaniciInfo(ogrNo)
            if aranan_kullanici == []:
                warning('Aranan Kullanıcı Bulunamadı').exec_()
            else:
                for row_number, row_data in enumerate(aranan_kullanici):
                    self.tableWidget_4.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget_4.setItem(
                            row_number, column_number, QtWidgets.QTableWidgetItem(str(row_data[data])))
                [i.clear() for i in [self.kullanici_ogr_no_2]]

        sender = self.sender()
        if sender.text() == "Kaydet":
            kullaniciEkle()

        elif sender.text() == "Ara":
            kullanici_ara()

        elif sender.text() == "Kullanıcı Bilgisi":
            kullanici_liste()

    def showWidget(self):
        # IS MENU OPEN OR CLOSE? | IS MENU OR SUB MENU | SET CSS
        def is_Open(is_first_menu, whichmenu):

            # adding last opened or closed menu for setting style css
            self.last_menu.append(whichmenu[0])

            if len(self.last_menu) > 3:
                self.last_menu.remove(self.last_menu[0])

            if self.open_close_control == "close":
                self.open_close_control = "open"

                if is_first_menu:
                    self.mainStack.setStyleSheet(
                        "QWidget{background:rgba(0,0,0,0.1)}")
                    return True
                else:
                    self.menuStack.hide()
                    self.mainStack.setStyleSheet(
                        "QWidget{background:rgba(0,0,0,0.0001)}")

            elif self.open_close_control == "open":
                if is_first_menu:
                    if self.last_menu[-1] == self.last_menu[-2]:
                        self.open_close_control = "close"
                        self.mainStack.setStyleSheet(
                            "QWidget{background:rgba(0,0,0,0.0001)}")
                        setCss([self.opened_menu[-1]])
                        return False
                    else:
                        self.open_close_control = "open"
                        self.menuStack.hide()
                        self.mainStack.setStyleSheet(
                            "QWidget{background:rgba(0,0,0,0.1)}")
                        return True
                else:
                    self.opened_menu.append(whichmenu[1])
                    self.mainStack.setStyleSheet(
                        "QWidget{background:rgba(0,0,0,0.0001)}")
                    self.menuStack.hide()

        def setCss(tabs):
            current_menu_css = "QPushButton{background:rgba(45,54,76,0.93);border:none;border-bottom:1px solid rgb(38,46,65);color:silver;font-size:28px;}QPushButton:hover{background:rgba(40,49,71,0.97);border:none;color:silver;border-bottom:1px solid rgb(38,46,65)}"
            current_submenu_css = "QPushButton{background:rgba(45,54,76,0.99);border:none;color:silver;font-size:18px;border-bottom:1px solid rgb(38,46,65)}QPushButton:hover{background:rgba(35,43,62,0.99);border:none;color:white;border-bottom:1px solid rgb(38,46,65)}"
            new_menu_css = "QPushButton{background:rgba(101,52,172,0.93);border:none;color:white;font-size:28px;border-top:none}"

            new_submenu_css = "QPushButton{background:rgba(101,52,172,0.93);border:none;color:silver;font-size:18px;}QPushButton:hover{background:rgba(91,47,155,0.97);border:none;color:white;}"
            menuList = [self.btn_profil, self.btn_kitap,
                        self.btn_odunc, self.btn_kullanici]
            subMenuList = [self.btn_kitap_kayit, self.btn_kitap_duzenle, self.btn_kitap_test, self.btn_odunc_ver,
                           self.btn_odunc_iade, self.btn_odunc_test, self.btn_kullanici_kayit, self.btn_kullanici_liste]


            tabs[0].setStyleSheet(new_menu_css)
            menuList.remove(tabs[0])
            tabs.remove(tabs[0])
            [theSubTabs.setStyleSheet(new_submenu_css) for theSubTabs in tabs]
            [subMenuList.remove(removedSubtab) for removedSubtab in tabs]
            [menu.setStyleSheet(current_menu_css) for menu in menuList]
            [subMenu.setStyleSheet(current_submenu_css)
             for subMenu in subMenuList]

        sender = self.sender()

        if sender.text() == "PROFİL":
            self.menuStack.hide()
            self.mainStack.setCurrentWidget(self.qw_profil)
            self.mainStack.setStyleSheet(
                "QWidget{background:rgba(0,0,0,0.001)}")
            is_Open(False, ["profil", self.btn_profil])
            setCss([self.btn_profil])

        elif sender.text() == "KİTAP\nİŞLEMLERİ":
            if is_Open(True, ["kitap", self.btn_kitap]):
                self.menuStack.setCurrentWidget(self.menu_kitap)
                self.menuStack.show()
                setCss([self.btn_kitap, self.btn_kitap_kayit,
                       self.btn_kitap_duzenle, self.btn_kitap_test])
            else:
                self.menuStack.hide()

        elif sender.text() == "ÖDÜNÇ\nİŞLEMLERİ":
            if is_Open(True, ["odunc", self.btn_odunc]):
                self.menuStack.setCurrentWidget(self.menu_odunc)
                self.menuStack.show()
                setCss([self.btn_odunc, self.btn_odunc_ver,
                       self.btn_odunc_iade, self.btn_odunc_test])
            else:
                self.menuStack.hide()

        elif sender.text() == "KULLANICI\nİŞLEMLERİ":
            if is_Open(True, ["kullanici", self.btn_kullanici]):
                self.menuStack.setCurrentWidget(self.menu_kullanici)
                self.menuStack.show()
                setCss([self.btn_kullanici, self.btn_kullanici_kayit,
                       self.btn_kullanici_liste])
            else:
                self.menuStack.hide()

        elif sender.text() == "KİTAP EKLE":
            self.kitapStack.setCurrentWidget(self.qw_kitap_ekle)
            self.mainStack.setCurrentWidget(self.qw_kitap)
            is_Open(False, ["kitap_ekle", self.btn_kitap])

        elif sender.text() == "KİTAP DÜZENLE":
            self.kitapStack.setCurrentWidget(self.qw_kitap_duzenle)
            self.mainStack.setCurrentWidget(self.qw_kitap)
            is_Open(False, ["kitap_duzenle", self.btn_kitap])

        elif sender.text() == "KİTAP LİSTESİ":
            self.kitapStack.setCurrentWidget(self.qw_kitap_test)
            self.mainStack.setCurrentWidget(self.qw_kitap)
            is_Open(False, ["kitap_test", self.btn_kitap])

        elif sender.text() == "ÖDÜNÇ VER":
            self.oduncStack.setCurrentWidget(self.qw_odunc_ver)
            self.mainStack.setCurrentWidget(self.qw_odunc)
            is_Open(False, ["odunc_ver", self.btn_odunc])

        elif sender.text() == "ÖDÜNÇ İADE":
            self.oduncStack.setCurrentWidget(self.qw_odunc_iade)
            self.mainStack.setCurrentWidget(self.qw_odunc)
            is_Open(False, ["odunc_iade", self.btn_odunc])

        elif sender.text() == "ÖDÜNÇ LİSTESİ":
            self.oduncStack.setCurrentWidget(self.qw_odunc_test)
            self.mainStack.setCurrentWidget(self.qw_odunc)
            is_Open(False, ["odunc_test", self.btn_odunc])

        elif sender.text() == "KULLANICI KAYIT":
            self.kullaniciStack.setCurrentWidget(self.qw_kullanici_kayit)
            self.mainStack.setCurrentWidget(self.qw_kullanici)
            is_Open(False, ["kullanici_kayit", self.btn_kullanici])

        elif sender.text() == "KULLANICI LİSTESİ":
            self.kullaniciStack.setCurrentWidget(self.qw_kullanici_listesi)
            self.mainStack.setCurrentWidget(self.qw_kullanici)
            is_Open(False, ["kullanici_listesi", self.btn_kullanici])

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


app = QApplication(sys.argv)
w = kutuphane()
w.show()
sys.exit(app.exec_())
