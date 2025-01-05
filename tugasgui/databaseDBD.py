import mysql.connector
"""
# Koneksi ke MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
cursor = db.cursor()

# Membuat database baru
cursor.execute("CREATE DATABASE IF NOT EXISTS shop")
print("Database 'shop' berhasil dibuat")
"""
# Koneksi ke database 'shop'
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="shop"
)
cursor = db.cursor()

sql = "UPDATE Customers SET FirstName=%s, LastName=%s, Email=%s WHERE Phone=%s"
val = ("Jaka", "Wijaya", "ibotsans@email.com", '081310116489')
cursor.execute(sql, val)

# Commit perubahan
db.commit()

# Menampilkan hasil update
print(cursor.rowcount, "record(s) affected")



# Membuat tabel Customers
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(15)
)
""")

# Mengisi data ke tabel Customers
cursor.execute("""
INSERT INTO Customers (FirstName, LastName, Email, Phone) VALUES
('John', 'Doe', 'john.doe@email.com', '1234567890'),
('Jane', 'Smith', 'jane.smith@email.com', '0987654321'),
('Alice', 'Johnson', 'alice.johnson@email.com', '5551234567'),
('Bob', 'Brown', 'bob.brown@email.com', '5559876543')
""")

# Membuat tabel Orders
cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    OrderDate DATE,
    CustomerID INT,
    TotalAmount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
)
""")

# Mengisi data ke tabel Orders
cursor.execute("""
INSERT INTO Orders (OrderDate, CustomerID, TotalAmount) VALUES
('2024-06-01', 1, 150.00),
('2024-06-02', 2, 250.00),
('2024-06-03', 3, 100.00),
('2024-06-04', 4, 200.00)
""")

# Membuat tabel Products
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(100),
    Price DECIMAL(10, 2),
    Stock INT
)
""")

# Mengisi data ke tabel Products
cursor.execute("""
INSERT INTO Products (ProductName, Price, Stock) VALUES
('Widget A', 50.00, 100),
('Widget B', 75.00, 200),
('Widget C', 100.00, 150),
('Widget D', 125.00, 50)
""")

# Membuat tabel OrderDetails
cursor.execute("""
CREATE TABLE IF NOT EXISTS OrderDetails (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    UnitPrice DECIMAL(10, 2),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
)
""")

# Mengisi data ke tabel OrderDetails
cursor.execute("""
INSERT INTO OrderDetails (OrderID, ProductID, Quantity, UnitPrice) VALUES
(1, 1, 2, 50.00),
(2, 2, 2, 3, 75.00),
(3, 3, 3, 1, 100.00),
(4, 4, 4, 2, 125.00)
""")

# Commit perubahan
db.commit()

print("Semua tabel dan data berhasil dibuat dan dimasukkan")

# Tutup koneksi
cursor.close()
db.close()
