import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="reivan17",
        database="antrian_rs"
    )
