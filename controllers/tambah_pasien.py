from flask import render_template, request, redirect, url_for
from models.pasien import tambah_pasien, cek_pasien_terdaftar

def tambah():
    if request.method == "POST":
        nama = request.form["nama"]
        umur = request.form["umur"]
        poli = request.form["poli"]

        if cek_pasien_terdaftar(nama):
            return render_template("tambah.html", error="Anda telah terdaftar.")

        nomor_antrian = tambah_pasien(nama, umur, poli)

        return redirect(url_for("konfirmasi", nama=nama, umur=umur, poli=poli, antrian=nomor_antrian))

    return render_template("tambah.html", error=None)
