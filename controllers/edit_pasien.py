from flask import render_template, request, redirect, url_for
from models.database import connect_db

def get_pasien_by_id(id_pasien):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM pasien WHERE id = %s", (id_pasien,))
    pasien = cursor.fetchone()
    db.close()
    return pasien

def update_pasien(id_pasien, nama, umur, poli):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("UPDATE pasien SET nama=%s, umur=%s, poli=%s WHERE id=%s", (nama, umur, poli, id_pasien))
    db.commit()
    db.close()

def edit(id_pasien):
    if request.method == "POST":
        nama = request.form["nama"]
        umur = request.form["umur"]
        poli = request.form["poli"]

        update_pasien(id_pasien, nama, umur, poli)

        return redirect(url_for("daftar_antrian"))

    pasien = get_pasien_by_id(id_pasien)
    if not pasien:
        return "Pasien tidak ditemukan!", 404 
    return render_template("edit.html", pasien=pasien)
