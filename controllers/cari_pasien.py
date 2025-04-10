from flask import render_template, request
from models.pasien import cari_pasien

def cari():
    keyword = request.args.get("keyword", "")
    hasil = cari_pasien(keyword)
    return render_template("antrian.html", pasien=hasil, pencarian=True)
