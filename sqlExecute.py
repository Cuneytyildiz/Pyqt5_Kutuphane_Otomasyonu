import re
from mysql.connector import MySQLConnection, connection


class sqlExecute():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.config = {
            'user': 'root',
            'password': '',
            'host': '127.0.0.1'
        }
        self.kitapData = {}
        self.kullaniciData = {}
        self.classData = {}

    def run_execute(self, sorgu):
        connection = MySQLConnection(**self.config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sorgu)
        connection.commit()
        connection.close()

    def fetch_execute(self, sorgu):
        connection = MySQLConnection(**self.config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sorgu)
        data = cursor.fetchall()
        connection.close()
        return data

    # ------------- Personel Başlangıç ------------- 
    def personelBilgi(self):
        return self.fetch_execute("select * from personel where kullanici_adi='{}'".format(self.username))

    def profilBilgi(self):
        return self.fetch_execute("select * from personel")
    
    def parolaDegistir(self,yeni):
        query = "UPDATE personel SET parola = '{}'"
        self.run_execute(query.format(yeni))

    # ------------- Personel Bitiş ------------- 
        

    # ------------- Kitap Başlangıç -------------
    def kitapEkle(self, kitapInfo):
        query = "insert into `kitap`(`kitap_adi`, `yazar_adi`, `yayinevi`, `tur`, `sayfa`, `basim`) values('{}','{}','{}','{}','{}','{}')"
        query = query.format(kitapInfo['kitap_adi'], kitapInfo['yazar_adi'],
                             kitapInfo['yayinevi'], kitapInfo['tur'], kitapInfo['sayfa'], kitapInfo['basim'])

        self.run_execute(query)

    def kitapBilgi(self):
        self.kitap_bilgi = []
        kitaplar = self.fetch_execute("select * from kitap")
        [self.kitap_bilgi.append(kitap['kitap_adi'] + " " + kitap['yazar_adi'] +
                                 " " + kitap['yayinevi']) for kitap in kitaplar]
        self.kitapData['kitapbilgi'] = self.kitap_bilgi
        return self.kitapData

    def kitapGuncelle(self, yeniKitapBilgi):
        query = "UPDATE `kitap` SET `yazar_adi`='{}',`yayinevi`='{}',`tur`='{}',`sayfa`='{}',`basim`='{}' WHERE kitap_adi = '{}'"
        self.run_execute(query.format(yeniKitapBilgi['yazar_adi'],
                         yeniKitapBilgi['yayinevi'], yeniKitapBilgi['tur'], yeniKitapBilgi['sayfa'], yeniKitapBilgi['basim'], yeniKitapBilgi['kitap_adi']))

    def KitapSil(self, kitapAdi):
        self.run_execute(
            "delete from `kitap` where kitap_adi= '{}'".format(kitapAdi))

    def KitapInfo(self, kitapAdi):
        return self.fetch_execute("select * from kitap where kitap_adi='{}'".format(kitapAdi))

    def KitapClass(self):
        kitapId = [i['kitap_id']
                   for i in self.fetch_execute("select kitap_id from kitap")]
        kitapId_yazar = [i['kitap_id']
                         for i in self.fetch_execute("select kitap_id from kitap")]
        kitapInfo = []
        for i in kitapId:
            if kitapId_yazar.count(i) < 1:
                a = self.fetch_execute(
                    "select kitap_adi,yazar_adi,yayinevi from kitap where kitap_id={}".format(i))
                kitapInfo.append(a[0]['kitap_adi']+" "+a[0]
                                 ['yazar_adi']+" "+a[0]['yayinevi'])
        return kitapInfo

    def KitapListe(self):
        return self.fetch_execute("select * from kitap")
    # ------------- Kitap Bitiş -------------


    # ------------- Kullanıcı Başlangıç -------------
    def KullaniciEkle(self, kullaniciData):
        query = "insert into `kullanici`(`ogrenci_no`, `ad`, `soyad`, `telefon_no`, `e_mail`) values('{}','{}','{}','{}','{}')"
        query = query.format(kullaniciData['ogrenci_no'], kullaniciData['ad'],
                             kullaniciData['soyad'], kullaniciData['telefon_no'], kullaniciData['e_mail'])
        self.run_execute(query)

    def KullaniciListe(self):
        return self.fetch_execute("select * from kullanici")

    def KullaniciInfo(self, ogrNo):
        return self.fetch_execute("select * from kullanici where ogrenci_no='{}'".format(ogrNo))

    def kullaniciBilgi(self):
        self.kullanici_bilgi = []
        kullanicilar = self.fetch_execute("select * from kullanici")
        [self.kullanici_bilgi.append(kullanici['ogrenci_no'] + " " + kullanici['ad'] +
                                     " " + kullanici['soyad']) for kullanici in kullanicilar]
        self.kullaniciData['kullanicibilgi'] = self.kullanici_bilgi
        return self.kullaniciData
    # ------------- Kullanıcı Bitiş-------------

    # ------------- Ödünç Başlangıç -------------
    def oduncEkle(self, oduncData, kitapId):
        query = "insert into `odunc`(`kitap_id`, `kitap_adi`, `yazar_adi`, `yayinevi`, `ogr_no`, `ad_soyad`, `telefon`, `alinma_tarih`) values('{}','{}','{}','{}','{}','{}','{}','{}')"
        query = query.format(oduncData['kitap_id'], oduncData['kitap_adi'],
                             oduncData['yazar_adi'], oduncData['yayinevi'], oduncData['ogr_no'], oduncData['ad_soyad'], oduncData['telefon'], oduncData['alinma_tarih'])
        query2 = "UPDATE kitap SET durum = 1  WHERE kitap_id = '{}'".format(
            kitapId)
        self.run_execute(query)
        self.run_execute(query2)

    def oduncInfo(self, kitapId):
        return self.fetch_execute("select * from kitap where kitap_id= '{}'".format(kitapId))

    def oduncBilgi(self):
        self.kitap_bilgi = []
        kitaplar = self.fetch_execute("select * from kitap where durum = 0")
        [self.kitap_bilgi.append(str(kitap['kitap_id']) + " " +
                                 kitap['kitap_adi'] + " " + kitap['yazar_adi']) for kitap in kitaplar]
        self.kitapData['kitapbilgi'] = self.kitap_bilgi
        return self.kitapData

    def iadeBilgi(self):
        self.iade_bilgi = []
        iadekitaplar = self.fetch_execute(
            "select * from odunc where teslim_tarihi = 'TESLİM EDİLMEDİ'")
        [self.iade_bilgi.append(str(kitap['odunc_id']) + " " +
                                kitap['ogr_no'] + " " + kitap['ad_soyad']+" "+kitap['kitap_adi']) for kitap in iadekitaplar]
        self.kitapData['iadebilgi'] = self.iade_bilgi
        return self.kitapData

    def iadeInfo(self, oduncId):
        return self.fetch_execute("select * from odunc where odunc_id= '{}'".format(oduncId))

    def iadeAra(self, ogrno):
        return self.fetch_execute("select * from odunc where ogr_no= '{}'".format(ogrno))

    def iadeEkle(self, oduncData, oduncId):
        query = "UPDATE odunc SET teslim_tarihi = '{}'  WHERE odunc_id = '{}'"
        self.run_execute(query.format(oduncData['teslim_tarihi'], oduncId))
        query2 = "UPDATE kitap SET durum = 0  WHERE kitap_id = '{}'".format(
            oduncData['kitap_id'])
        self.run_execute(query2)

    def oduncListe(self):
        return self.fetch_execute("select * from odunc")
    # ------------- Kullanıcı Bitiş -------------

    # ------------- Veritabanı Oluşturma Başlangıç -------------
    def register(self, dictData):
        self.db_name = self.username
        try:
            query0 = "create database %s character set utf8 collate utf8_turkish_ci;" % (
                self.db_name)
            query1 = "create table personel(kullanici_adi VARCHAR(50),parola VARCHAR(30),ad VARCHAR(300),soyad VARCHAR(20), e_mail VARCHAR(30),telefon_no VARCHAR(30));"
            query2 = "create table kitap(kitap_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,kitap_adi VARCHAR(50),yazar_adi VARCHAR(50),yayinevi VARCHAR(50),tur VARCHAR(50),sayfa INT, basim VARCHAR(80),durum INT DEFAULT '0');"
            query3 = "create table kullanici(kullanici_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,ogrenci_no VARCHAR(50),ad VARCHAR(100),soyad VARCHAR(100),telefon_no VARCHAR(30),e_mail VARCHAR(30));"
            query4 = "create table odunc(odunc_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,kitap_id INT NOT NULL,kitap_adi VARCHAR(50) NOT NULL,yazar_adi VARCHAR(50) NOT NULL,yayinevi VARCHAR(50) NOT NULL,ogr_no VARCHAR(50) NOT NULL,ad_soyad VARCHAR(100) NOT NULL, telefon VARCHAR(100) NOT NULL, alinma_tarih VARCHAR(100) NOT NULL, teslim_tarihi VARCHAR(100) DEFAULT 'TESLİM EDİLMEDİ')"

            for query in [query0, query1, query2, query3, query4]:
                self.run_execute(query)
                self.config['database'] = '%s' % (self.db_name)

            userInsert = "INSERT INTO `personel`(`kullanici_adi`, `parola`, `ad`, `soyad`, `e_mail`, `telefon_no`) VALUES('{}','{}','{}','{}','{}','{}')"
            userInsert = userInsert.format(dictData['kullanici_adi'], dictData['parola'],
                                           dictData['ad'], dictData['soyad'], dictData['e_mail'], dictData['telefon_no'])
            self.run_execute(userInsert)

        except:
            print(dictData['kullanici_adi'], "adlı bir kullanıcı var")
    # ------------- Veritabanı Oluşturma Bitiş -------------

    # ------------- Giriş Verisi Başlangıç -------------
    def login(self):
        not_get = ["information_schema",
                   "performance_schema", "phpmyadmin", "mysql"]
        db = [i['Database'] for i in self.fetch_execute("SHOW DATABASES;")]
        #[db.remove(i) for i in not_get]
        # is the username exist?
        if db.count(self.username) > 0:
            self.config['database'] = self.username
            # is the password correct?
            real_password = [i['parola'] for i in self.fetch_execute(
                "select parola from personel where kullanici_adi='{}'".format(self.username))][0]

            return (True if real_password == self.password else False)
        else:
            return False
    # ------------- Giriş Verisi Bitiş -------------