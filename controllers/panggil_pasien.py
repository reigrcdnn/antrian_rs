from flask import render_template
from models.pasien import panggil_pasien

def panggil():
    pasien = panggil_pasien()
    return render_template("panggil.html", pasien=pasien)
