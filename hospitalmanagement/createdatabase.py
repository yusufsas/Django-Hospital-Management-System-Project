import sqlite3

# Veritabanı bağlantısını oluştur
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Hastalar tablosunu oluştur
cursor.execute('''CREATE TABLE IF NOT EXISTS hastalar (
                    HastaID INTEGER PRIMARY KEY,
                    Ad TEXT,
                    Soyad TEXT,
                    DogumTarihi DATE,
                    Cinsiyet TEXT,
                    TelefonNumarasi TEXT,
                    Adres TEXT
                )''')

# Doktorlar tablosunu oluştur
cursor.execute('''CREATE TABLE IF NOT EXISTS doktorlar (
                    DoktorID INTEGER PRIMARY KEY,
                    Ad TEXT,
                    Soyad TEXT,
                    UzmanlikAlani TEXT,
                    CalistigiHastane TEXT
                )''')

# Randevular tablosunu oluştur
cursor.execute('''CREATE TABLE IF NOT EXISTS randevular (
                    RandevuID INTEGER PRIMARY KEY,
                    RandevuTarihi DATE,
                    RandevuSaati TEXT,
                    HastaID INTEGER,
                    DoktorID INTEGER,
                    FOREIGN KEY (HastaID) REFERENCES hastalar(HastaID),
                    FOREIGN KEY (DoktorID) REFERENCES doktorlar(DoktorID)
                )''')

# Tıbbi Raporlar tablosunu oluştur
cursor.execute('''CREATE TABLE IF NOT EXISTS tibbi_raporlar (
                    RaporID INTEGER PRIMARY KEY,
                    RaporTarihi DATE,
                    RaporIcerigi TEXT,
                    RaporURL TEXT,
                    HastaID INTEGER,
                    DoktorID INTEGER,
                    FOREIGN KEY (HastaID) REFERENCES hastalar(HastaID),
                    FOREIGN KEY (DoktorID) REFERENCES doktorlar(DoktorID)
                )''')

# Veritabanı değişikliklerini kaydet ve bağlantıyı kapat
conn.commit()
conn.close()
