import mysql.connector

# Koneksi ke MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = db.cursor()    

# Membuat database baru
cursor.execute("CREATE DATABASE IF NOT EXISTS Toko")
print("Database 'shop' berhasil dibuat")