
import mysql.connector
import os

mydb = mysql.connector.connect(
    host = "localhost",
    user= "Jaka Kelana",
    password= "jakawijaya29",
    database="SistemNescafe"
    
)
print(mydb)




import tkinter as tk
from tkinter import messagebox
import mysql.connector

def create_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="Jaka Kelana",
        password="jakawijaya29",
        database="SistemNescafe"
    )
    mycursor = conn.cursor()
    mycursor.execute('''CREATE TABLE IF NOT EXISTS users(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))''')
    conn.commit()
    conn.close()

def register():
    username = entry_username.get()
    password = entry_password.get()

    conn = mysql.connector.connect(
        host="localhost",
        user="Jaka Kelana",
        password="jakawijaya29",
        database="SistemNescafe"
    )
    mycursor = conn.cursor()
    mycursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    conn.close()

    messagebox.showinfo("Registration", "Registrasi Berhasil!")

def login():
    username = entry_username.get()
    password = entry_password.get()

    conn = mysql.connector.connect(
        host="localhost",
        user="Jaka Kelana",
        password="jakawijaya29",
        database="SistemNescafe"
    )
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = mycursor.fetchone()
    conn.close()

    if user:
        messagebox.showinfo("Login", "Login Berhasil!")
    else:
        messagebox.showerror("Login", "Invalid username or password")

create_table()

root = tk.Tk()
root.configure(bg="#3498db")

root.title("Login Nescafe")

label_username = tk.Label(root, text="Username:", bg="#3498db", fg="#ffffff")
label_username.grid(row=0, column=0, padx=10, pady=10)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:", bg="#3498db", fg="#ffffff")
label_password.grid(row=1, column=0, padx=10, pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

btn_register = tk.Button(root, text="Register", command=register, bg="#2ecc71", fg="#ffffff")
btn_register.grid(row=2, column=0, padx=10, pady=10)

btn_login = tk.Button(root, text="Login", command=login, bg="#2ecc71", fg="#ffffff")
btn_login.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
