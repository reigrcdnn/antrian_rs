from models.pasien import get_antrian
from flask import render_template

def antrian():
    data = get_antrian()
    return render_template("antrian.html", pasien=data)
