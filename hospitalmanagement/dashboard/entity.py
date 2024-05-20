import sqlite3
from datetime import date

# Initialize the database connection
def connect_db():
    return sqlite3.connect('db.sqlite3')

# Create tables
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS AdminAcc (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Ad TEXT,
        Soyad TEXT,
        password TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Hasta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        HastaID TEXT,
        Ad TEXT,
        Soyad TEXT,
        DogumTarihi DATE,
        Cinsiyet TEXT,
        TelefonNumarasi TEXT,
        Adres TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Doktor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        DoktorID TEXT,
        Ad TEXT,
        Soyad TEXT,
        UzmanlikAlani TEXT,
        CalistigiHastane TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Randevu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        RandevuTarihi DATE,
        RandevuSaati TEXT,
        Hasta_id INTEGER,
        Doktor_id INTEGER,
        FOREIGN KEY(Hasta_id) REFERENCES Hasta(id),
        FOREIGN KEY(Doktor_id) REFERENCES Doktor(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS TibbiRapor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        RaporTarihi DATE,
        RaporIcerigi TEXT,
        RaporImage TEXT,
        Hasta_id INTEGER,
        Doktor_id INTEGER,
        FOREIGN KEY(Hasta_id) REFERENCES Hasta(id),
        FOREIGN KEY(Doktor_id) REFERENCES Doktor(id)
    )
    ''')

    conn.commit()
    conn.close()

# Insert data into AdminAcc
def insert_admin_acc(ad, soyad, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO AdminAcc (Ad, Soyad, password) VALUES (?, ?, ?)', (ad, soyad, password))
    conn.commit()
    conn.close()

# Insert data into Hasta
def insert_hasta(hasta_id, ad, soyad, dogum_tarihi, cinsiyet, telefon_numarasi, adres):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Hasta (HastaID, Ad, Soyad, DogumTarihi, Cinsiyet, TelefonNumarasi, Adres) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                   (hasta_id, ad, soyad, dogum_tarihi, cinsiyet, telefon_numarasi, adres))
    conn.commit()
    conn.close()

# Insert data into Doktor
def insert_doktor(doktor_id, ad, soyad, uzmanlik_alani, calistigi_hastane):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Doktor (DoktorID, Ad, Soyad, UzmanlikAlani, CalistigiHastane) VALUES (?, ?, ?, ?, ?)', 
                   (doktor_id, ad, soyad, uzmanlik_alani, calistigi_hastane))
    conn.commit()
    conn.close()

# Insert data into Randevu
def insert_randevu(randevu_tarihi, randevu_saati, hasta_id, doktor_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Randevu (RandevuTarihi, RandevuSaati, Hasta_id, Doktor_id) VALUES (?, ?, ?, ?)', 
                   (randevu_tarihi, randevu_saati, hasta_id, doktor_id))
    conn.commit()
    conn.close()

# Insert data into TibbiRapor
def insert_tibbi_rapor(rapor_tarihi, rapor_icerigi, rapor_image, hasta_id, doktor_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO TibbiRapor (RaporTarihi, RaporIcerigi, RaporImage, Hasta_id, Doktor_id) VALUES (?, ?, ?, ?, ?)', 
                   (rapor_tarihi, rapor_icerigi, rapor_image, hasta_id, doktor_id))
    conn.commit()
    conn.close()

# Update functions
def update_admin_acc(id, ad, soyad, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE AdminAcc SET Ad = ?, Soyad = ?, password = ? WHERE id = ?', (ad, soyad, password, id))
    conn.commit()
    conn.close()

def update_hasta(id, hasta_id, ad, soyad, dogum_tarihi, cinsiyet, telefon_numarasi, adres):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Hasta SET HastaID = ?, Ad = ?, Soyad = ?, DogumTarihi = ?, Cinsiyet = ?, TelefonNumarasi = ?, Adres = ? WHERE id = ?', 
                   (hasta_id, ad, soyad, dogum_tarihi, cinsiyet, telefon_numarasi, adres, id))
    conn.commit()
    conn.close()

def update_doktor(id, doktor_id, ad, soyad, uzmanlik_alani, calistigi_hastane):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Doktor SET DoktorID = ?, Ad = ?, Soyad = ?, UzmanlikAlani = ?, CalistigiHastane = ? WHERE id = ?', 
                   (doktor_id, ad, soyad, uzmanlik_alani, calistigi_hastane, id))
    conn.commit()
    conn.close()

def update_randevu(id, randevu_tarihi, randevu_saati, hasta_id, doktor_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Randevu SET RandevuTarihi = ?, RandevuSaati = ?, Hasta_id = ?, Doktor_id = ? WHERE id = ?', 
                   (randevu_tarihi, randevu_saati, hasta_id, doktor_id, id))
    conn.commit()
    conn.close()

def update_tibbi_rapor(id, rapor_tarihi, rapor_icerigi, rapor_image, hasta_id, doktor_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE TibbiRapor SET RaporTarihi = ?, RaporIcerigi = ?, RaporImage = ?, Hasta_id = ?, Doktor_id = ? WHERE id = ?', 
                   (rapor_tarihi, rapor_icerigi, rapor_image, hasta_id, doktor_id, id))
    conn.commit()
    conn.close()

# Delete functions
def delete_admin_acc(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM AdminAcc WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def delete_hasta(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Hasta WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def delete_doktor(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Doktor WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def delete_randevu(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Randevu WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def delete_tibbi_rapor(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM TibbiRapor WHERE id = ?', (id,))
    conn.commit()
    conn.close()

# Filter functions
def filter_admin_acc_by_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM AdminAcc WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result

def filter_hasta_by_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Hasta WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result
def filter_hasta_by_hastaid(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Hasta WHERE HastaID = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result

def filter_doktor_by_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Doktor WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result
def filter_doktor_by_doktorid(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Doktor WHERE DoktorID = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result
def filter_randevu_by_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Randevu WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result

def filter_tibbi_rapor_by_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM TibbiRapor WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result

# Run the create tables function
create_tables()
