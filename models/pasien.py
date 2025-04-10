from models.database import connect_db
from models.database import connect_db

def cek_pasien_terdaftar(nama):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM pasien WHERE nama = %s AND status = 'Menunggu'", (nama,))
    jumlah = cursor.fetchone()[0]
    db.close()
    return jumlah > 0


def get_nomor_antrian():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM pasien")
    jumlah = cursor.fetchone()[0]
    db.close()
    return jumlah + 1

def tambah_pasien(nama, umur, poli):
    nomor_antrian = get_nomor_antrian()
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO pasien (nama, umur, poli, status) VALUES (%s, %s, %s, 'Menunggu')", (nama, umur, poli))
    db.commit()
    db.close()
    return nomor_antrian

def get_antrian():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, nama, umur, poli FROM pasien WHERE status='Menunggu' ORDER BY id ASC")
    data = cursor.fetchall()
    db.close()
    return data

def panggil_pasien():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, nama, umur, poli FROM pasien WHERE status='Menunggu' ORDER BY id ASC LIMIT 1")
    pasien = cursor.fetchone()

    if pasien:
        cursor.execute("UPDATE pasien SET status='Dilayani' WHERE id=%s", (pasien[0],))
        db.commit()
        db.close()
        return pasien
    db.close()
    return None

def cari_pasien(keyword):
    db = connect_db()
    cursor = db.cursor()
    query = "SELECT id, nama, umur, poli FROM pasien WHERE status='Menunggu' AND (nama LIKE %s OR poli LIKE %s)"
    cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
    hasil = cursor.fetchall()
    db.close()
    return hasil
