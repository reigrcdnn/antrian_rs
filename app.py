import webview
import threading
import os
import signal

from flask import Flask, render_template, request, redirect, url_for
from controllers.tambah_pasien import tambah
from controllers.lihat_antrian import antrian
from controllers.panggil_pasien import panggil
from controllers.cari_pasien import cari
from controllers.edit_pasien import edit


app = Flask(__name__, template_folder="views", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tambah", methods=["GET", "POST"])
def tambah_pasien():
    return tambah()

@app.route("/antrian")
def daftar_antrian():
    return antrian()

@app.route("/panggil")
def panggil_pasien():
    return panggil()

@app.route("/cari")
def cari_pasien():
    return cari()

@app.route("/edit/<int:id_pasien>", methods=["GET", "POST"])
def edit_pasien(id_pasien):
    return edit(id_pasien)

@app.route("/konfirmasi")
def konfirmasi():
    nama = request.args.get("nama")
    umur = request.args.get("umur")
    poli = request.args.get("poli")
    antrian = request.args.get("antrian")
    return render_template("konfirmasi.html", nama=nama, umur=umur, poli=poli, antrian=antrian)

def run_flask():
    app.run(debug=True, use_reloader=False)

@app.route("/keluar", methods=["POST"])
def keluar():
    os.kill(os.getpid(), signal.SIGTERM)  
    return "Aplikasi ditutup", 200

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    webview.create_window("Aplikasi Antrian RS", "http://127.0.0.1:5000")
    webview.start()

