"""
import time
start_time = time.time()
print("hello")
a=20
print(a)
print("jaka")
print("waduh")
for i in range(1,1000):
    a=20


#python3 -m py_compile Main.py
if __name__=="__main__":
    #program kedua
    def add(x,y):
        return x+y
    def subtract (x,y):
        return x-y
    def divide(x,y):
        return x/y
    def multiply(x,y):
        return x*y
    num1 = float(input("enter the first number : "))
    num2 = float(input("enter the second number: "))
    operation=input("enter the operation(+,-,*,/): ")

    if operation == "+":
        result = add(num1,num2)
    elif operation == "-":
        result = subtract(num1,num2)
    elif operation == "*":
        result = multiply(num1,num2)
    elif operation == "/":
        result = divide(num1,num2)
    else:
        print("invalid operation")
    print(result)
print(time.time() - start_time,"detik")
"""
"""
# variabel adalah tempat menyimpan data

#menaru/assignment nilai
a = 10
x = 5
panjang = 100

#pemanggilan pertama
print("Nilai pertama =", a)
print("Nilai kedua = ", x)
print("panjang jembatan =", panjang)

# penamaan
nilai_y = 15 # dengan menggunakan underscore
print(nilai_y)
juta10 = 100000 #sabi
print(juta10)
nilaiZ = 17,5
print(nilaiZ)
#pemanggilan kedua 
print("nilai pertama: ",a)
a = 19
print("nilai baru:  ", a)

#assignment indirect
b = a
print("Nilai Bagus: ", b)

#Tipe data: Angka satuan (integer)
data_integer = 1000
print("Data: ",data_integer)
print("bertipe",type(data_integer))
#tipe data: float

data_float = 10.5
print("Data: ",data_float)
print("bertipe",type(data_float))

#tipe data: string kumpulan karakter
data_string = "JakaKelana"
print("Data: ",data_string)
print("bertipe",type(data_string))

#tipe data: boolean true/false 

data_bool = True
print("Data: ",data_bool)
print("bertipe",type(data_bool))

## tipe data khusus

#bilangan kompleks

data_complex = complex(10,5)
print("Data: ",data_complex)
print("bertipe",type(data_complex))

# tipe dari dari bahasa C

from ctypes import c_double

data_c_double = c_double(12.5)
print("Data: ",data_c_double)
print("bertipe",type(data_c_double))

# casting tipe data
#merubah tipe data ke tipe data lain
# tipe data = int,float,str,bool

## integer
print("=====INTEGER=====")
data_int = 29;
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data = ",data_int,"type = ",type(data_int))
print("data = ",data_float,"type = ",type(data_float))
print("data = ",data_str,"type = ",type(data_str))
print("data = ",data_bool,"type = ",type(data_bool)) #akan false jika nilai int = 0

## float
print("====FLOAT=====")
data_float = 17.5
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ",data_float,"type = ",type(data_float))
print("data = ",data_int,"type = ",type(data_int))
print("data = ",data_str,"type = ",type(data_str))
print("data = ",data_bool,"type = ",type(data_bool)) # akan false jika nilai float 0

# BOOLEAN
print("====BOOLEAN====")
data_bool = True;
data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("data = ",data_bool,"type = ",type(data_bool))
print("data = ",data_int,"type = ",type(data_int))
print("data = ",data_str,"type = ",type(data_str))
print("data = ",data_float,"type = ",type(data_float))

# String
print("====STRING====")
data_str = "18";
data_int = int(data_str) # string harus angka
data_float = float(data_str) # string harus angka
data_bool = bool(data_str) #false jika kosong
print("data = ",data_str,"type = ",type(data_str))
print("data = ",data_int,"type = ",type(data_int))
print("data = ",data_bool,"type = ",type(data_bool))
print("data = ",data_float,"type = ",type(data_float))

#Mengambil data dari user

#data yang di masukkan pasti string

data = input("Masukkan nama: ")
data1 = input("Masukkan NIM: ")
data2 = input("Nilai matkul: ")
print("nama: ",data,"type = ",type(data))
print(" NIM: ",data1,"type = ",type(data1))
print("Nilai: ",data2,"type = ",type(data2))
#Jika ingin mengambil int/float maka:
angka = int(input("masukkan NIM: "))
angka2 = float(input("masukkan nilai: "))
print("NIM: ",angka,"type: ",type(angka))
print("NIlai: ",angka2,"type: ",type(angka2))

# part Boolean 
biner = bool(int(input("masukkan nilai bool: ")))
print("data = ",biner,"type = ",type(biner))
# rangkuman
data = input("nilai matkul: ")
print("nilai: ",data,"type = ",type(data))
angka = bool(int(input("nilai matkul: ")))
print("nilai",angka,"type = ",type(angka))


#operasi aritmatika

a = 12
b = 3

#pertambahan
hasil = a + b
print(a,'+',b,'=',hasil)
#pengurangan
hasil = a - b
print(a,'-',b,'=',hasil)
#perkalian
hasil = a * b
print(a,'*',b,'=',hasil)
#pembagian 
hasil = a / b
print(a,'/',b,'=',hasil)
#eksponen (pangkat)
hasil = a ** b
print(a,'**',b,'=',hasil)
#operasi modulus %
hasil = a % b
print(a,'%',b,'=',hasil)
#operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

#prioritas operasi

# 1.() 2.exponen ** 3.perkalian dan teman2 * / % // 4. + dan -

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x ** y * z
print(x,'**' ,y, '*',z,'=',hasil) 
# kurung akan mengambil langkah pertama
hasil = (x+y)*z
print('(',x,'+',y,') *',z,'=',hasil)

# latihan konversi satuan konversi 

# program konversi celcius ke satuan lain 

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius =float(input("masukkan nilai suhu dalam celcius :"))
print("suhu adalah =",celcius,"Celcius")

#Reamur
reamur = (4/5) * celcius
print("suhu dalam =",reamur,"Reamur")

#Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam =",fahrenheit,"Fahrenheit")

#kelvin
kelvin = celcius + 273 
print("suhu dalam = ",kelvin,"K")

# task 1 (konversi suhu)
print("\nKONVERSI TEMPERATUR FAHRENHEIT&KELVIN\n")
fahrenheit = float(input("Masukkan suhu dalam fahrenheit:"))
print("suhu adalah = ",fahrenheit,"F")

#fahrenheit to kelvin 
Rumus = (fahrenheit - 32) * 5/9 + 273.15
print("suhu dalam kelvin : ",Rumus,"K")

#kelvin to fahrenheit
Kelvin = float(input("Masukkan suhu dalam Kelvin:"))
print("suhu adalah = ",Kelvin,"K")
rumus = (Kelvin - 273.15) * 9/5 + 32 
print("suhu dalam fahrenheit = ",rumus,"F")


print("Nama: Jaka Kelana Wijaya")
print("Nim: 11103223048")
print("No.hp: 081310116489")
print("Alamat: Sukabumi")
 
ip = float(input("Masukan nilai ip : "))

if ip >= 3.5:
    print("Selamat anda lulus dengan ipk: ",ip)
else : 
    print("Anda lulus dengan ip sebesar :",ip)
print("semangat")

ip = float(input("Masukkan nilai anda : "))
if ip < 1.5 :
    print("maaf anda tidak lulus karena ipk anda : ",ip)
elif ip < 3.5 :
    print("selamat anda lulus dengan ipk ",ip)
else :
    print("selamat anda lulus cumlaude",ip)
print("info loker")
    
SEA=["Makan","coding","sleep","repeat"]
for kegiatan in SEA :
    print(kegiatan)
for x in range (4):
    print(x)
   
x = int(input("Masukkan banyak perulangan: "))
y=0
while y < x :
    print("jaka Kelana Wijaya")
    y=y+1

x = 0
y = 0

for x in range (5):
    for y in range (5):
        if(y<=x):
            print('*', end='  '   )
    print("  ")


x="jaka kelana"
for name in x :
    print(name)
    if name==x[4]:
         break 
print(name)
Habits=["subuh","makan","coding","tidur","repeat"]
for actions in Habits:
    if actions==Habits[2]:
         continue
print(actions)

baju_nama = str(input("Masukkan nama baju : "))
print("Nama baju :",baju_nama,"tipe baju : ","type = ",type(baju_nama))
harga_baju = float(input("masukkan harga baju : "))
print("Harga baju :",harga_baju,"tipe baju : ","type = ",type(harga_baju))
jumlah_baju = int(input("Masukkan jumlah baju :"))
print("jumlah baju :",harga_baju,"type =",type(jumlah_baju))
jumlah_bayar = float(input("masukkan jumlah bayar :"))
print("jumlah bayar :",jumlah_bayar,"type =",type(jumlah_bayar)) 

# operasi aritmatika
total_harga = harga_baju * jumlah_baju
kembalian = jumlah_bayar - total_harga

print("Total yang harus di bayar",total_harga)
print("Kembaliannya = ",kembalian)

a = 20.5
b = 30.5
c = 40.5
d = 50.5
print("Nilai a =",a)
print("Nilai b =",b)
print("Nilai c =",c)
print("Nilai d =",d)
a = 20.5
b = 30.5
c = 40.5
d = 50.5
#pertukaran
a, b, c, d = b, d, a, c
print("Setelah pertukaran:")
print("Nilai a =", a)
print("Nilai b =", b)
print("Nilai c =", c)
print("Nilai d =", d)

if a >= b and a >= c and a >= d:
    nilai_terbesar = a
elif b >= a and b >= c and b >= d:
    nilai_terbesar = b
elif c >= a and c >= b and c >= d:
    nilai_terbesar = c
else:
    nilai_terbesar = d

print("Nilai terbesar adalah:", nilai_terbesar)
#urutan variable dari yang terbesar -> terkecil
urutan = [a, b, c, d]
#menggunakan metode sort dgn parameter reverse true
urutan.sort(reverse=True)

print("Nilai  terbesar ke terkecil:")
for nilai in urutan:
    print(nilai)


nama = "jaka kelana wijaya"
print("nama = ",nama)
nim  = 1103223048
print("nim = ",nim)

import random

tugas_1 = random.randint(51,100)
tugas_2 = random.randint(51,100)
tugas_3 = random.randint(51,100)
tugas_4 = random.randint(51,100)
tugas_5 = random.randint(51,100)
tugas_6 = random.randint(51,100)

print("tugas 1: ",tugas_1)
print("tugas 2: ",tugas_2)
print("tugas 3: ",tugas_3)
print("tugas 4: ",tugas_4)
print("tugas 5: ",tugas_5)
print("tugas 6: ",tugas_6)

Clo1 = (tugas_1 + tugas_2)/2
Clo2 = (tugas_3 + tugas_4 )/2
Clo3 = (tugas_5 + tugas_6)/2

print("nilai CLO1 =",Clo1)
print("nilai Clo2 =",Clo2)
print("nilai Clo3 =",Clo3)

nilai_akhir = (Clo1+Clo2+Clo3)/3
print("nilai akhir =",nilai_akhir)
if nilai_akhir > 80:
    print("index = ",'A')
elif nilai_akhir > 70 :
    print("index =",'B')
elif nilai_akhir > 60:
    print("index =",'C')
else :
    print("inde =",'D')
"""


"""
angka = 1
while True:
    if (angka % 2 == 0):
        #angka genap
        #print("angka =",angka,"adalah bilangan genap")
        angka += 1
    else :
        #angka ganjil
        print("angka = ",angka,"adalah bilangan ganjil")
        angka += 1
    if angka >= 10:
        break
"""
 
"""     
#latihan 1
#membuat kotak % 5 baris 5 kolom
baris = 5 #jumlah baris 

for i in range (baris):
    print('%'*baris)
"""    

"""
#menggunakan for 
baris = 5
count = 5
for i in range(baris):
    print('%'*count)
    count -=1
"""

"""
#menggunakan while
baris = 5
count= 1

while  True:
    print('%' * count)
    count +=1
    if count > baris :
     break
"""
"""
bintang = 8 
for i in range(bintang):
  for j in range(i+1):
    print(' ',end='')
  for k in range(bintang-i):
    print('* ',end='')
  print()
"""

"""
angka = 1
while True:
    if (angka % 2 == 0):
        print("angka = ",angka,"adalah bilangan ganjil")
    angka += 1
    if angka >= 10:
        break
"""

"""
bintang = 8
for i in range(bintang):
  for k in range(i+1):
    print(' ',end=(' '))
"""
"""
Jaka_list = [1, 2, 3, 4, 5]
print(Jaka_list)
jaka_dict = {'nama': 'jaka', 'usia': 19, 'kota': 'Bandung'}
print(jaka_dict)
"""
"""
Jaka_list = [1, 2, 3]
Jaka_list.append(4)

print(Jaka_list)
jaka_dict = {'nama': 'Jaka', 'usia': 19}
nama = jaka_dict.get('nama')
alamat = jaka_dict.get('alamat', 'Alamat tidak tersedia')
age = jaka_dict.get('usia')
print(age)

jaka_dict = {}
jaka_dict['kunci1'] = 'nilai1'
jaka_dict['kunci2'] = 'nilai2'
# Menambahkan elemen lain
jaka_dict['kunci3'] = 'nilai3'
# Menghapus elemen 'kunci2'
del jaka_dict['kunci2']

print(jaka_dict)  # Output: {'kunci1': 'nilai1', 'kunci3': 'nilai3'}
"""
""""
# Fitur.clear()
print(">>> Fitur .Clear()")
status_mahasiswa = {'nama' : 'jaka kelana','NIM' : '1103223048','Fakultas' : 'Teknik elektro'}
status_mahasiswa.clear()
print(status_mahasiswa)

# Fitur copy
print(">>> Fitur .Copy()")
status_mahasiswa1 = {'nama' : 'jaka kelana','NIM' : '1103223048','Fakultas' : 'Teknik elektro'}
status_mahasiwa2 = status_mahasiswa1.copy()
status_mahasiwa2 ['nama'] = 'ujang'
status_mahasiwa2 ['NIM'] = '111132221'
print(status_mahasiswa1)
print(status_mahasiwa2)

#Fitur keys
print(">>> Fitur .keys()")
status_mahasiswa = {'nama' : 'jaka kelana','NIM' : '1103223048','Fakultas' : 'Teknik elektro'}
kunci_akses = list(status_mahasiswa.keys())
print(kunci_akses)

#Fitur Values
print(">>> Fitur .Values()")
status_mahasiswa = {'nama' : 'jaka kelana','NIM' : '1103223048','Fakultas' : 'Teknik elektro'}
value_dict = list(status_mahasiswa.values())
print(value_dict)

#Fitur update
print(">>> Fitur .update()")
status_mahasiswa = {'nama' : 'jaka kelana','NIM' : '1103223048','Fakultas' : 'Teknik elektro'}
status_mahasiswa.update({'skillset' : ['python','c','Java']})
print(status_mahasiswa)
"""
"""
#LIST
handphone = ["iphone","vivo","oppo","samsung","nokia"]
print(handphone[3])
print(handphone[1:5])

#MENGGANTI DATA PADA LIST
handphone[3]="Xiaomi"
for x in (handphone): 
    print(x,end=' ')

#MENAMBAHKAN DATA PADA LIST
handphone.append("Redmi")
print(handphone)

#MENAMBAHKAN DUA LIST MENJADI SATU
list_1 = ['x','y','z']
list_2 = ['1','2','3']
list_3 = list_1 + list_2
print(list_3)

#MENGURUTKAN DATA PADA LIST
handphone.sort()
print(handphone)
handphone.sort(reverse=True)
print(handphone)

#TUPLE
#TUple dengan satu tipe data

#membuat tuple berisi angka
tuple_angka = (1,2,3,4)
print(tuple_angka)
#membuat tuple berisi huruf
tuple_huruf = ("Welcome","to","SEA")
print(tuple_huruf)
#tuple banyak tipe
tuple =(29,3.14,"JAKA","SEA")
print(tuple)

#Mengakses data pada TUPLE
#1. menggunakan Indeks

angka_genap = (2,4,6,8,10,12)
#Mengakses tuple angka pada indeks ke pertama
print("indeks pertama :",angka_genap[0])
#Mengakses tuple angka pada indeks ke tiga
print("indeks ketiga :",angka_genap[2])
#Mengakses tuple angka pada indeks ke lima
print("indeks kelima :",angka_genap[4])

#2. Menggunakan Unpacking
angka_ganjil = (1,3,5,7)
#unpacking elemen pada angka ganjil
a,b,c,d = angka_ganjil
print(a)
print(b)
print(c)
print(d)

#Menggabungkan 2 tuple (Conccateanation)
tuple1 = (3,2,1)
tuple2 = ("Welcome","to","SEA")
#Conccateanation tuple 1 dan 2
tuple3 = tuple2+tuple1
#menampilkan ketiga tuple dan liat perbedaannya
print(tuple1)
print(tuple2)
print(tuple3)

#Mengiris Tuple Slicing
tuple_angka = (1,2,3,4,5,6)
#slicing tuple angka menghapus angka pertama
print(tuple_angka[1:])
#slicing tuple angka menampilkan 3 angka pertama
print(tuple_angka[0:3])
#slicing tuple angka menghapus angka terakhir
print(tuple_angka[:5])

#Menghapus tuple(Delete)
tuple0=("good","Morning","SEA")
print(tuple0)
del tuple0
print("hapus")


#Mengurutkan elemen tuple(Sorting)
tuple_angka = (6,25,26,14,65,230,669,54,26,1,53)
print(tuple_angka)
tuple_new = sorted(tuple_angka)
print(tuple_new)

#SET

#Menambahkan Data dalam SET
#Fungsi add()
buah = {"mangga","apel","Anggur"} #inisialisasi set
buah.add("tomat") #menambahkan data baru dalam set
print(buah) #menampilkan

#fungsi update()
buah = {"apel","mangga","jeruk"}
buah.update(["cabe","sawo"])
print(buah)

#Menghapus data di dalam set
#Fungsi remove

buah = {"tomat","apel","mangga","jeruk"}
buah.remove("tomat")
print(buah)
buah.discard("apel")
print(buah)
buah.clear()
print(buah)

#Menggabungkan 2 set menjadi 1
set1= {"1","2","3"}
set2= {"a","b","c"}
set1.update(set2)
print(set1)

#DICTIONARY
dict1 ={1:"kalkulus",2:"PBO",3:"Matvek"}
dict2 ={"indonesia":1,"Malaysia":2,"singapura": 3}
print(dict1)
print(dict2)

biodict = dict ({"nama": "jaka","age": 19})
print(biodict)

#elemen Add()
biodict = {}
print(biodict)
#menambahkan elemen
biodict["nama"] = "Jaka"
biodict["usia"] = "19"
biodict["work"] = "football player"
print(biodict)
#mengupdate elemen
biodict["work"] = "Enginer"
print(biodict)

#Mengakses Elemen
biodict = dict({"nama": "jaka","usia": "19","work": "developer"})
print(biodict["nama"])
print(biodict["usia"])
#Menggunakan fungsi get
dict1 ={1:"kalkulus",2:"PBO",3:"Matvek"}
print(dict1.get(1))
print(dict1.get(2))

#Menghapus Elemen
dict1 ={1:"kalkulus",2:"PBO",3:"Matvek"}
print(dict1)
del dict1[1]  #Menggunakan metode del
print(dict1)
del dict1[2]
print(dict1)

#Menggunakan metode pop
dict1 ={1:"kalkulus",2:"PBO",3:"Matvek"}
print(dict1)
dict1.pop(1)  
print(dict1)
dict1.pop(2)
print(dict1)

#Menngunakan popitem
dict1 ={1:"kalkulus",2:"PBO",3:"Matvek"}
print(dict1)
dict1.popitem()
dict1.popitem()
print(dict1)

#Menggunakan metode clear
dict1 ={1:"kalkulus",2:"PBO",3:"Matvek"}
print(dict1)
dict1.clear()
print(dict1)
"""
"""
x = [[1, 5, 9],
     [2, 3, 7],
     [4, 6, 8]]

print(x)		#menampilkan semua nilai x
print(x[0][1])	#menampilkan baris ke-1 kolom ke-2
print(x[2])     #Menampilkan baris ke-3

"""

"""
n = int(input("Masukkan nilai n: "))  # Meminta input dari pengguna

# Inisialisasi variabel untuk menyimpan jumlah bilangan genap
jumlah_genap = 0

# Melakukan perulangan dari 1 hingga n
for i in range(1, n + 1):
    if i % 2 == 0:
        jumlah_genap += i

# Mencetak jumlah bilangan genap
print(f"Jumlah bilangan genap dari 1 hingga {n} adalah: {jumlah_genap}")

angka = 1
for i in range (angka,11):
    print(i)


nilai = int(input("masukkan nilai: "))
if nilai > 0 :
    print("positif")
elif nilai < 0 :
    print("negatif")
else :
    print("nol")
"""
"""
kendaraan = ["mobil", "motor", "truk"]

# tampilkan kata yang tersimpan pada variabel
for vehicle in  kendaraan:
  print(vehicle)

nomer = [0,222,6,-1,3]
for i in nomer:
    if (i < 0):
       print("mendekati negatif")
       break
    print(nomer)
for x in range (5):
   print(x)
for y in range(3,8,2):
   print(y)
jawab = 'ya'
hitung = 0
while(True):
   hitung +=1
   jawab = input("ulang?")
   print("total perulangan: ",(hitung))
   if jawab >= 1 :
       break
"""
# IF ELSE STATEMENT
"""
nama = input("Masukkan nama : ")

# IF inline
if nama == "kelana" : print("Kelana wijaya")
print(f"Terima kasih {nama}")
# IF indentation

if nama == "Kato" :
    print("Megumi Kato")
    print("Teknik Komputer")
print(f"Terima kasih {nama}")

# Else Statement

if nama == "jaka":
    print("Mahasiswa Telkom ")
else :
    print("Anda bukan mahasiswa telkom")   
print("akhir dari program") 
"""
"""
x= 5

while(x > 2):

     print(x)

     x = x-1

C=1

C = C + 1

C += 10
print(C)    

X = [2,3]

Y = [4,2]

Hasil= Y + X
print(Hasil)

i = 1

while i < 6:

   print(i)

   if (i == 3):

      break

   i += 1

cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)

fruits =  ("apple", "banana","cherry","manggo", "guava")
for x in fruits: 
    if x!="banana": 
      print(x)

array = [1, 2, 3]

print(sum(array)) 

print('1' + '2')

x= [1,2,3]

x+= [1,1,1]
print(x)

x = 21

if x > 10:

   print("Above ten")

   if x > 20:

      print("And also above 20!")

else:

    print("But not above 20.")


x = 1

y = 2

z = 3

a = str(x) + str(y) + str(z)

print(a)

c=[9,7,8,5]
c[0]=10
print(c)

x = "banana"
for [x] in "banana": print([x])
"""
#Fungsi
# Syntax 
# def nama_fungsi(parameter):
    #statement kode
#nama_fungsi(parameter  )
#Fungsi return
"""
def kali(a,b):
    return a*b
y = kali(4,5)
print("hasil = ",y)

def luas_persegi(a):
    return a*a
x = int(input("masukkan angka: "))
luas_persegi(x)
print("hasil =",luas_persegi(x))
#Fungsi tanpa return

def kali(a,b):
    print("hasil =",a*b)
kali (5,5)
  
def luas_segitiga(a,t):
    luas = a*t*0.5
    print(f"luas segitiga = {luas: .2f}")
x = int(input("masukkan angka sisi : "))
y = int(input("masukkan angka tinggi :"))
luas_segitiga(x,y)

#variabel Global
#variabel lokal

lebar = 50 #variable Global

def hitung_persegipanjang(panjang):
    return lebar*panjang

def hitung_persegi():
    panjang_persegi = 100 #variable lokal
    return lebar*panjang_persegi
print(hitung_persegipanjang(50))
print(hitung_persegi())

#CLASS
#syntax
# Class Nama_class:
    #statement kode
class Mahasiswa:
    universitas = "Tel U"
    def __init__(self,nama,nim) :
        self.nama = nama
        self.nim = nim
mahasiswa1 = Mahasiswa("Jaka Kelana",1103223048)
print(f"Nama :  {mahasiswa1.nama}")
print(f"Nim :   {mahasiswa1.nim}")
print(f"Universitas :{mahasiswa1.universitas}")        

class persegi_panjang:
    def __init__(self,panjang,tinggi):
        self.panjang = panjang
        self.tinggi = tinggi
    def luas(self):
        return self.panjang*self.tinggi
    def keliling(self):
        return (self.panjang*2)+(self.tinggi*2)
pp = persegi_panjang(int(input("masukkan panjang: ")),int(input("masukkan tinggi :")))
print(pp.luas())
print(pp.keliling())
"""
#Inheritance 
#syntax
# class NamakelasTurunan (Nama kelas Induk):

#Kelas induk

"""
class Satuan :
    def __init__(self):
        self.sisi = 6
#Kelas turunan

class persegi(Satuan):
    def __init__(self):
        super().__init__()
        self.keliling =self.sisi*4
    def getluas(self):
        self.luas = int(self.sisi)* int(self.sisi)
        print("luas persegi =",self.luas)
    def getkeliling(self):
        print("luas keliling",self.keliling) 

object=persegi()
object.getluas()
object.getkeliling()
#calling inheritance
Var = persegi()
Var.getluas()

# Access Modifier Inheritance
#syntax
# public -> def namafungsi(self):
# protected -> def _namafungsi(self):
# private -> def __namafungsi(self):

#Single Inheritance

"""
"""
class parent:
    def func1(self):
        print("ini fungsi ada pada kelas utama")
class anak:
    def func2(self):
        print("fungsi ini ada pada kelas turunan ")
object = parent()
object.func1()
object = anak()
object.func2()

#Multiple Inheritance

class ibu:
    nama_ibu = ""
    def ibu(self):
        print(self.nama_ibu)
class ayah :
    nama_ayah = ""
    def ayah(self):
        print(self.nama_ayah)
class anak(ibu,ayah):
    def orang_tua(self):
        print("Ayah :",self.nama_ayah)
        print("ibu",self.nama_ibu)
keluarga = anak()
keluarga.nama_ayah = "Asep sunandar"
keluarga.nama_ibu = "silvilla"
keluarga.orang_tua()


"""
"""
class barang :
    def getbarang1 (self):
        self.hargasebelumganti =  10000
        print("Harga sebelum ganti = ",self.hargasebelumganti)

    def _getbarang2(self):
        self.hargaseudahdiganti = 20000
        print("harga sesudah diganti: ",self.hargaseudahdiganti)
    
object = barang()
object.getbarang1()
object._getbarang2()
"""

"""
class Data :
    def __init__(self):
        self._harga = 20000
    def _ganti(self,harga_baru):
        self._harga = harga_baru
class Barang(Data):
    def tampilkan_harga(self):
         print("harga sebelum diganti = ",self._harga)
         self._ganti(10000)
         print("harga sesudah diganti =",self._harga)
    
object = Barang()
object.tampilkan_harga()
"""
"""
class Kampus:
    def __init__(self):
        self.nama_mahasiswa = "Richard"
        self.umur_mahasiswa = 20
        self.nim_mahasiswa = 1103223048

        self.nama_dosen = "Agus"
        self.umur_dosen = 50
        self.nidn_dosen = 10101010110

class TampilkanData(Kampus):
    def tampilkan_data(self):
        print("Data Mahasiswa:")
        print("Nama:", self.nama_mahasiswa)
        print("Umur:", self.umur_mahasiswa)
        print("NIM:", self.nim_mahasiswa)

        print("\nData Dosen:")
        print("Nama:", self.nama_dosen)
        print("Umur:", self.umur_dosen)
        print("NIDN:", self.nidn_dosen)

object = TampilkanData()
object.tampilkan_data()
"""
"""
class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def deskripsi(self):
        print(f'Hewan {self.nama} adalah jenis {self.jenis}')

# Membuat objek hewan
satwa = Hewan("Harimau", "Karnivora")

# Memanggil metode deskripsi
satwa.deskripsi()
"""

"""
def penjumlahan(x,y):
        return x+y
def pengurangan(x,y):
        return x-y
def pembagian(x,y):
        return x/y
def perkalian(x,y):
        return x*y
def modulus(x,y):
        return x%y
def pemangkatan(x,y):
        return x**y
        
num1 = float(input("masukkan angka pertama : "))
num2 = float(input("masukkan angka kedua : "))
operation=input("enter the operation(+,-,*,/,%,**): ")

if operation == "+":
        result = penjumlahan(num1,num2)
elif operation == "-":
        result = pengurangan(num1,num2)
elif operation == "*":
        result = perkalian(num1,num2)
elif operation == "/":
        result = pembagian(num1,num2)
elif operation == "%":
        result = modulus(num1,num2)
elif operation == "**":
        result = pemangkatan(num1,num2)
else:
    print("invalid operation")
print(result)
"""
"""
# deklarasi fungsi dengan argumen i=baris j=kolom
def fungsi_1 (i,j):
  for i in range(j):
    print("*" * i)
    i +=1

def fungsi_2 (i,j):
  for i in range(j):
    print(" " * j + "*" * i)
    j -=1
def fungsi_3(i, j):
    for k in range(j):
        print(" " * (j-k-1) + "*" * (k+1))
def fungsi_4(i, j):
    for k in range(j):
        print(" " * k + "*" * (j-k))






  

# input pilih fungsi
pilih = input("pilih fungsi tangga = ")

# percabangan ketika memilih fungsi
if (pilih == '1'):
  fungsi_1(1, 4) #masukan jumlah i dan j sebagai argumen disini

elif(pilih == '2'):
  fungsi_2(1, 4)
elif(pilih == '3'):
  fungsi_3(1,4)
elif(pilih == '4'):
   fungsi_4(1,4)
else:
  print("salah input")
"""
"""
nameList = ["Luthfi", "Nissa", "Leonardo", "Caprio", "Raihan", "Dewa"]
nameList.append("Ariana")
print(nameList)
    
fruits = ("apple", "banana","cherry","manggo","guava",)
for x in fruits : 
   if x!="banana": 
      print(x)
   


N= 0
for x in range(2, 20, 3):
   if x%2==0 :
      N = N + x
   else:
     N
print(N)

bil_list = [3,8,6,4,10]
print(sorted(bil_list))
"""
"""
import random

quiz_1 = random.randint(50,100)
quiz_2 = random.randint(50,100)
quiz_3 = random.randint(50,100)

nilai_rata = (quiz_1+quiz_2+quiz_3)/3

if nilai_rata > 80 :
    indeks = "A"
elif nilai_rata > 70 :
    indeks = "B"
elif nilai_rata > 60 :
    indeks = "C"
else :
    print("indeks = D")
print(f"Nilai rata-rata:{nilai_rata}")
print(f"Indeks: {indeks}")
"""
"""
import random

clo1=[random.randint(0,100) for _ in range(5)]
del clo1[2]
clo1.append(100)
clo1.sort(reverse=True)
print(clo1)

def penjumlahan(x,y):
        return x+y
def pengurangan(x,y):
        return x-y
def pembagian(x,y):
        return x/y
def perkalian(x,y):
        return x*y
def modulus(x,y):
        return x%y
def pemangkatan(x,y):
        return x**y
print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Modulus")
print("6. Pemangkatan")

pilihan = input("Masukkan nomor operasi (1/2/3/4/5/6): ")        
num1 = float(input("masukkan angka pertama : "))
num2 = float(input("masukkan angka kedua : "))


if pilihan == "1":
        result = penjumlahan(num1,num2)
elif pilihan == "2":
        result = pengurangan(num1,num2)
elif pilihan == "3":
        result = perkalian(num1,num2)
elif pilihan == "4":
        result = pembagian(num1,num2)
elif pilihan == "5":
        result = modulus(num1,num2)
elif pilihan == "6":
        result = pemangkatan(num1,num2)
else:
    print("invalid operation")
print(result)
"""
"""
def fungsi_1():
    for baris in range(7):
        print("*" * 7)

def fungsi_2():
    for baris in range(7):
        if baris >= 1 and baris <= 5:
            print("" + " " * 5 + "")
        else:
            print("*" * 7)

def fungsi_3():
    for baris in range(7):
        if baris == 1 or baris == 2 or baris == 4 or baris == 5:
            print("" + " " * 2 + "" + " " * 2 + "*")
        else:
            print("*" * 7)

def fungsi_4():
    for baris in range(7):
        if baris == 1 or baris == 2 or baris == 4 or baris == 5:
            print("" + " " * 5 + "")
        elif baris == 3:
            print("" + " " * 2 + "" + " " * 2 + "*")
        else:
            print("*" * 7)

pilihan = int(input("Pilih fungsi: "))

if pilihan == 1:
    fungsi_1()
elif pilihan == 2:
    fungsi_2()
elif pilihan == 3:
    fungsi_3()
elif pilihan == 4:
    fungsi_4()
"""
"""
def cetak_pola(pilihan):
    for baris in range(7):
        if pilihan == 1:
            print("*" * 7)
        elif pilihan == 2:
            if baris >= 1 and baris <= 5:
                print("     ")
            else:
                print("*" * 7)
        elif pilihan == 3:
            if baris == 1 or baris == 2 or baris == 4 or baris == 5:
                print("  " + "  *")
            else:
                print("*" * 7)
        elif pilihan == 4:
            if baris == 1 or baris == 2 or baris == 4 or baris == 5:
                print("     ")
            elif baris == 3:
                print("  " + "  *")
            else:
                print("*" * 7)
        else:
            print("Pilihan tidak valid.")

pilihan = int(input("Pilih fungsi (1/2/3/4): "))

cetak_pola(pilihan)
"""
"""
# Override

class Parent(object):
    def override(self): #Fungsi pertama
        print("ini adalah fungsi override() dari kelas parent")
class Child(Parent):
    def override(self): #fungsi turunan menimpa fungsi utama dengan nama yang sama
        print("ini adalah fungsi override() dari kelas child")
class Child2(Child):
    def override(self): #fungsi turunan kedua yg menimpa fungsi sebelumny
        print("ini adalah fungsi override() kelas child 2")

dad = Parent()
son = Child()
daughter = Child2()

dad.override()
son.override()
daughter.override()
"""
"""
#Overload
class Penjumlahan():
    def add(self,a,b):
        return a*b 
    def add(self,a,b,c):
        return a*b*c
object = Penjumlahan()
#print(object.add(1,2))
print(object.add(1,2,3))
"""

"""
class Penjumlahan:
    def add(self, *args):
        result = 0
        for i in args:
            if type(i) == int:
                result += i
        return result

# Membuat objek dari kelas Penjumlahan
objek = Penjumlahan()

# Memanggil metode add dan mencetak hasilnya
print(objek.add(2, 1, 10))
print(objek.add(3, 1))
"""
"""
class Toko:
    def __init__(self, nama):
        self.nama_pembeli = nama
        self._pensil = 0
        self._pulpen = 0
        self._penggaris = 0
        self._hargapensil = 2500
        self._hargapulpen = 7600
        self._hargapenggaris = 8500
        self._jumlahharga = 0
        self._jumlahbarang = 0

    def cekbarang(self):
        print(f"Jumlah pensil: {self._pensil}")
        print(f"Jumlah pulpen: {self._pulpen}")
        print(f"Jumlah penggaris: {self._penggaris}")

    def cekharga(self):
        print(f"Harga pensil: Rp {self._hargapensil}")
        print(f"Harga pulpen: Rp {self._hargapulpen}")
        print(f"Harga penggaris: Rp {self._hargapenggaris}")

    def barang(self, pensil, pulpen, penggaris, hargapensil, hargapulpen, hargapenggaris):
        self._pensil = pensil
        self._pulpen = pulpen
        self._penggaris = penggaris
        self._hargapensil = hargapensil
        self._hargapulpen = hargapulpen
        self._hargapenggaris = hargapenggaris

    def _total(self):
        self._jumlahbarang = self._pensil + self._pulpen + self._penggaris
        self._jumlahharga = (
            self._pensil * self._hargapensil +
            self._pulpen * self._hargapulpen +
            self._penggaris * self._hargapenggaris
        )

    def cekakhir(self):
        self._total()
        print(f"Total harga: Rp {self._jumlahharga}")
        print(f"Total barang: {self._jumlahbarang}")


jaka_toko = Toko("Jaka")
jaka_toko.barang(2, 3, 1, 2500, 7600, 8500)
jaka_toko.cekbarang()
jaka_toko.cekharga()
jaka_toko.cekakhir()

"""
"""
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost", #nama host di localhost 
  user="Jaka Kelana", #nama user di localhost 
  password="jakawijaya29" #nama pass di localhost
)

print(mydb)
#membuat database

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE databasePBO")

#check isi db
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

mydb = mysql.connector.connect(
  host= "localhost", #nama host di localhost 
  user= "Jaka Kelana", #nama user di localhost 
  password= "jakawijaya29", #nama pass di localhost
  database= "databasePBO" #nama database di localhost
)

# Membuat tabel
mycursor = mydb.cursor()

# Contoh: Membuat tabel 'test' dengan kolom 'id'
mycursor.execute("CREATE TABLE IF NOT EXISTS test (id INT(10) AUTO_INCREMENT PRIMARY KEY)")

# Contoh: Membuat tabel 'customers' dengan kolom 'id' dan 'name'
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT(10) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# Menampilkan tabel-tabel dalam database
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

mydb = mysql.connector.connect(
  host= "localhost", #nama host di localhost 
  user= "Jaka Kelana", #nama user di localhost 
  password= "jakawijaya29", #nama pass di localhost
  database= "databasePBO" #nama database di localhost
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

mycursor = mydb.cursor()

#mycursor.execute("SELECT name FROM customers")
mycursor.execute("SELECT address FROM customers")


myresult = mycursor.fetchall()

for x in myresult:
  print(x)
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

#sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
"""
"""
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user= "Jaka Kelana",
    password= "jakawijaya29",
    database= "Sistemlogin "
)

"""
"""
cursor = db.cursor()
cursor.execute('CREATE DATABASE Sistemlogin')
print("database done")
"""

"""
if db.is_connected():
    print("done")
"""
"""
#TKinter
from tkinter import*
from tkinter import ttk
root = Tk()
ttk.Button(root,text="Jaka kelana").grid()
root.mainloop()

import tkinter
main_window = tkinter.Tk()
label=tkinter.Label(main_window,text="Absen cuy")

label.pack()
main_window.mainloop()

#label dan button

import tkinter
main_window = tkinter.Tk()

def event_hadir():
    label2=tkinter.Label(main_window,text="selamat bekerja")
    label2.pack()
label= tkinter.Label(main_window,text="program absen cuy")
tombol = tkinter.Button(main_window,text="ADA cuy",command=event_hadir)

label.pack()
tombol.pack()
main_window.mainloop()
"""
'''
from tkinter import*
from tkinter import messagebox

root= Tk()
root.title("program kasir!")
root.geometry("600x440")

username = "jakakelana"
password = "apaaja"

def login():
    user = e1.get()
    pas = e2.get()

    if(username == user and password == pas):
        messagebox.showinfo("halaman admin","selamat anda berhasil login")
    else:
        messagebox.showwarning("gagal","anda salah bjir")
#membuat tabel

Label = Label(root,text="log in kasir cuy!")
Label.pack()

#membuat entry atau inputan
e1 = Entry(root)
e1.pack()
e1.insert(0," ")

e2= Entry(root)
e2.pack()
e2.insert(0," ")

#membuat button
tombol = Button(root,text="login",command=login)
tombol.pack()
root.mainloop()
'''
"""
class player:
    name = 'mbok jamu'

    def getName(self):
        return self.name
pemain=player()
print(pemain)

class player:
    name ='mbok jj '

    def getName(self):
        return self.name
pemain = player()
print(pemain.getName())


class Player:
    name = ''
    speed = ''
    
    def __init__(self,name,speed): 
        self.name = name
        self.speed = speed
     
    def getName(self):
        return self.name
    def getSpeed(self):
        return self.speed
    
        
pemain = Player('Lorenzo','86')
pemain2 = Player('Messi','76')
pemain3 = Player('ronaldo','99')
print(pemain.getName()+ " punya speed " + pemain.getSpeed())
print(pemain2.getName()+ " punya speed " + pemain2.getSpeed())
print(pemain3.getName()+ "punya speed"+pemain3.getSpeed())

class Karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print("Total karyawan:", Karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)

# Membuat objek pertama dari kelas Karyawan
karyawan1 = Karyawan("Sarah", 1000000)
# Membuat objek kedua dari kelas Karyawan
karyawan2 = Karyawan("Budi", 2000000)
karyawan3 = Karyawan("jaka",10000000)

karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
karyawan3.tampilkan_profil()
print("Total karyawan :", Karyawan.jumlah_karyawan)
"""
"""
class harga:
    def __init__(self,panjang,lebar,harga_permeter):
        self.panjang = panjang
        self.lebar = lebar
        self.harga_permeter = harga_permeter

    def hitungharga(self):
        luas = self.panjang*self.lebar
        return luas * self.harga_permeter
    def tampilkandata(self):
        print("panjang tanah=",self.panjang)
        print("lebar tanah=",self.lebar)
        print("harga tanah permeter=",self.harga_permeter)

hasil = harga(100,200,350000)  
hasil.tampilkandata()
print("maka harga tanah =", hasil.hitungharga())
"""
"""
class Orang:
    def __init__(self,fname,lname):
        self.namadepan = fname
        self.namabelakang = lname

    def cetak(self):
            print(self.namadepan, self.namabelakang)
class mahasiswa(Orang):
    pass

x = mahasiswa("asep","jaka")
x.cetak()
"""
"""
class barang :
    def __init__(self,nama_barang,hargapengiriman,panjang,lebar,tinggi,tujuan):
        self.namabarang = nama_barang
        self.hargabarang = hargapengiriman
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.tujuan = tujuan
    def volume(self):
        return (self.panjang*self.lebar*self.tinggi)/6000
    
class pengiriman(barang):
    def __init__(self,nama_barang,panjang,lebar,tinggi,tujuan,lama_pengiriman):
        super().__init__(nama_barang,panjang,lebar,tinggi,tujuan)
        self.lamapengiriman = lama_pengiriman
    def hitung_biaya(self):
        volume= (self.volume())
        tarif = 12500
        return volume * tarif*self.lamapengiriman

barang1=pengiriman(nama_barang="helm",panjang=40,lebar=30,tinggi=10,tujuan="Semarang",lama_pengiriman=3)
barang2=pengiriman(nama_barang="lemari",panjang=100,lebar=70,tinggi=120,tujuan="Jakarta",lama_pengiriman=2)

biaya_barang1= barang1.hitung_biaya()
biaya_barang2= barang2.hitung_biaya()

print(f"Biaya pengiriman{barang1.namabarang}ke{barang1.tujuan}:Rp{biaya_barang1}")
print(f"Biaya pengiriman{barang2.namabarang}ke{barang2.tujuan}:Rp{biaya_barang2}")
"""
"""
class Barang:
    def __init__(self, nama_barang, panjang, lebar, tinggi, tujuan):
        self.namabarang = nama_barang
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.tujuan = tujuan

    def volume(self):
        return (self.panjang * self.lebar * self.tinggi) / 6000

class Pengiriman(Barang):
    def __init__(self, nama_barang, panjang, lebar, tinggi, tujuan, lama_pengiriman):
        super().__init__(nama_barang, panjang, lebar, tinggi, tujuan)
        self.lamapengiriman = lama_pengiriman

    def hitung_biaya(self):
        volume = self.volume()
        tarif = 12500
        return volume * tarif * self.lamapengiriman

barang1 = Pengiriman(nama_barang="helm", panjang=40, lebar=30, tinggi=10, tujuan="Semarang", lama_pengiriman=3)
barang2 = Pengiriman(nama_barang="lemari", panjang=100, lebar=70, tinggi=120, tujuan="Jakarta", lama_pengiriman=2)

biaya_barang1 = barang1.hitung_biaya()
biaya_barang2 = barang2.hitung_biaya()

print(f"Informasi Pengiriman {barang1.namabarang}:")
print(f"Ukuran: {barang1.panjang} x {barang1.lebar} x {barang1.tinggi}")
print(f"Tujuan: {barang1.tujuan}")
print(f"Lama Pengiriman: {barang1.lamapengiriman} hari")
print(f"Biaya pengiriman {barang1.namabarang} ke {barang1.tujuan}: Rp {biaya_barang1}")

print(f"Informasi Pengiriman {barang2.namabarang}:")
print(f"Ukuran: {barang2.panjang} x {barang2.lebar} x {barang2.tinggi}")
print(f"Tujuan: {barang2.tujuan}")
print(f"Lama Pengiriman: {barang2.lamapengiriman} hari")
print(f"Biaya pengiriman: Rp {biaya_barang2}")
"""
"""
#Database mysql

import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password="",

)
if db.is_connected():
    print("success")

"""
"""
#membuat database 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)
conn = db.cursor()
conn.execute("CREATE DATABASE sulthon")
print("done bang") 

"""
"""
#Mengecek database
import mysql.connector

# Connect to the MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="seantuy"  # Specify your database name
)
# Create a cursor object
conn = db.cursor()
# Execute the SQL query to show databases
conn.execute("SHOW DATABASES")
# Fetch all the databases
list_db = conn.fetchall()
# Print the list of databases
list_db = [i[0] for i in list_db]
for i in list_db:
    print(i)
"""
#CRUD (create,read,update,delete)

#Membuat table(create)
"""
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="seantuy"

)
conn = db.cursor()
table_conten= ''' CREATE TABLE Madrid_FC (
    nama INT AUTO_INCREMENT PRIMARY KEY,
    pace VARCHAR(255),
    nomer VARCHAR(255),
    umur INT

)
'''
conn.execute(table_conten)
print("done bang")
"""
#Mengisi table insert
"""
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="seantuy"

)
conn = db.cursor()
data_table = "INSERT INTO madrid_FC (pace,nomer,umur)VALUES (%s,%s,%s)"
value = [
    ('Ronaldo',99,7),
    ('benzema',87,9),
    ('Bale',97,11),
]
for val in value:
    conn.execute(data_table,val)
    db.commit()

#membaca isi table read

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="seantuy"

)

conn = db.cursor()
conn.execute("SELECT * FROM madrid_FC")
data = conn.fetchall()

for x in data:
    print(x)
"""
"""
#mengubah isi tabel(update)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="seantuy"

)

conn = db.cursor()
ganti = "UPDATE madrid_FC SET pace=%s,nomer=%s,umur=%s WHERE pace = %s "
ganti_nama=("Mbappe",99,9,"benzema")
conn.execute(ganti,ganti_nama)

db.commit()
conn.execute("SELECT * FROM madrid_FC")
tampilkan = conn.fetchall()

for x in tampilkan:
    print(x)
"""   
# Delete 
"""
import mysql.connector 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="seantuy"

)
conn = db.cursor()
delete = "DELETE FROM madrid_FC WHERE nama = %s"
val = (2,)
conn.execute(delete,val)
db.commit()
conn.execute("SELECT * FROM madrid_FC")
tampilkan = conn.fetchall()

for x in tampilkan:
    print(x)
"""
#menghapus table
"""
import mysql.connector 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="seantuy"

)
conn = db.cursor()
conn.execute("DROP TABLE madrid_FC")
print("tabel dihapus") 
"""
"""
#menghapus database

import mysql.connector 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="seantuy"

)
conn = db.cursor()
conn.execute("DROP DATABASE seantuy")
print("database dihapus") 
"""
"""
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)
conn = db.cursor()
conn.execute("CREATE DATABASE Barudak")
print("done bang") 
"""
"""
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Barudak"

)
conn = db.cursor()
table_content= ''' CREATE TABLE mahasiswa (
    Teman INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(255),
    nim VARCHAR(255)
)
'''
conn.execute(table_content)
print("done bang")
"""
"""
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Barudak"

)
conn = db.cursor()
data_table = "INSERT INTO mahasiswa (nama,nim)VALUES (%s,%s)"
value = [
    ('Ridho',1103223077),
    ('asep',1103223069),
    ('sutisna',11102020),
]
for val in value:
    conn.execute(data_table,val)
    db.commit()
conn.close()
db.close()
print("insert data done kang")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Barudak"

)
conn = db.cursor()
delete = "DELETE FROM mahasiswa WHERE Teman = %s"
val = (36,)
conn.execute(delete,val)
db.commit()

conn.execute("SELECT * FROM mahasiswa ")
tampilkan = conn.fetchall()
for x in tampilkan:
    print(x)

conn.close()
db.close()
print("Delete data done kang")
"""

import mysql.connector
"""
db = mysql.connector.connect(
     host = "localhost",
     user = "root",
     password = "",
 )
if db.is_connected():
     print("Connecetion seccessful")

db = mysql.connector.connect(
     host = "localhost",
     user = "root",
     password = "",
)

real = db.cursor()
real.execute("CREATE DATABASE turnamen")
print("Database created successfully")
"""
"""
db = mysql.connector.connect(
     host = "localhost",
     user = "root",
     password = "",
     database = "turnamen"
)
real = db.cursor()
table_content = '''CREATE TABLE roaster (
     id_valorant INT AUTO_INCREMENT PRIMARY KEY,
     nama VARCHAR(255),
     role VARCHAR(255),
     nim INT
)
'''
real.execute(table_content)
print("Table created")
"""
"""
db = mysql.connector.connect(
     host = "localhost",
     user = "root",
     password = "",
     database = "turnamen" 
)
real = db.cursor()

data_table = "INSERT INTO roaster (nama, role, nim ) VALUES (%s, %s, %s)"
value = [
     ('NASY','initiator',1103223136),
     ('CocaFanta','Duelist',1103223136),
     ('Kai','Initiator',1103223136),
     ('Woo','Controller',1103223136),
     ('Ahok','Sentinel',1103223136),
]

for val in value : 
     real.execute(data_table, val)
     db.commit()
     

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "turnamen" 
)
real = db.cursor()
data_delete = "DELETE FROM roaster WHERE id_valorant = %s"
val = (13,)
real.execute(data_delete, val)

db.commit()

real.execute("SELECT * FROM roaster")
data = real.fetchall()

for x in data:
    print(x) 

import mysql.connector 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="turnamen"

)
conn = db.cursor()
conn.execute("DROP DATABASE turnamen")
print("database dihapus") 
"""

"""
class BangunDatar:
    def __init__(self, panjang=0, lebar=0, tinggi=0, sisi=0, alas=0, radius=0):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.sisi = sisi
        self.alas = alas
        self.radius = radius

class Square(BangunDatar):
    def __init__(self, panjang=0, lebar=0, sisi=0):
        super().__init__(panjang=panjang, lebar=lebar, sisi=sisi)

    def luas_persegi(self):
        return self.panjang * self.lebar

    def keliling_persegi(self):
        return self.sisi * 4

class Triangle(BangunDatar):
    def __init__(self, alas=0, tinggi=0, sisi=0):
        super().__init__(alas=alas, tinggi=tinggi, sisi=sisi)

    def luas_segitiga(self):
        return 0.5 * self.alas * self.tinggi

    def keliling_segitiga(self):
        return self.sisi + self.sisi + self.sisi

class Circle(BangunDatar):
    def __init__(self, radius=0):
        super().__init__(radius=radius)

    def hitung_luas(self):
        return 3.14 * self.radius ** 2

    def hitung_keliling(self):
        return 2 * 3.14 * self.radius


persegi = Square(2,2,2)
print("PERSEGI:")
print("Luas Persegi = ", persegi.luas_persegi())
print("Keliling Persegi = ", persegi.keliling_persegi())

segitiga = Triangle(2, 6, 8)
print("\nSEGITIGA:")
print("Luas Segitiga = ", segitiga.luas_segitiga())
print("Keliling Segitiga = ", segitiga.keliling_segitiga())

lingkaran = Circle(5)
print("\nLINGKARAN:")
print("Luas Lingkaran = ", lingkaran.hitung_luas())
print("Keliling Lingkaran = ", lingkaran.hitung_keliling())
"""

"""
class Mahasiswa:
    def __init__(self, kode_kelas, dosen_wali, jumlah_mahasiswa):
        self.kode_kelas = kode_kelas
        self.dosen_wali = dosen_wali
        self.jumlah_mahasiswa = jumlah_mahasiswa


class MahasiswaKelas(Mahasiswa):
    def __init__(self, kode_kelas, dosen_wali, jumlah_mahasiswa, nama, nim, nilai_matkul1, nilai_matkul2, nilai_matkul3):
        super().__init__(kode_kelas, dosen_wali, jumlah_mahasiswa)
        self.nama = nama
        self.nim = nim
        self.nilai_matkul1 = nilai_matkul1
        self.nilai_matkul2 = nilai_matkul2
        self.nilai_matkul3 = nilai_matkul3

    def hitung_rata_rata(self):
        return (self.nilai_matkul1 + self.nilai_matkul2 + self.nilai_matkul3) / 3

    def tampilkan_info(self):
        print(f"Nama Mahasiswa: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Kode Kelas: {self.kode_kelas}")
        print(f"Dosen Wali: {self.dosen_wali}")
        print(f"Jumlah Mahasiswa: {self.jumlah_mahasiswa}")
        print(f"Nilai Matkul 1: {self.nilai_matkul1}")
        print(f"Nilai Matkul 2: {self.nilai_matkul2}")
        print(f"Nilai Matkul 3: {self.nilai_matkul3}")
        print(f"Rata-rata Nilai Matkul: {self.hitung_rata_rata()}")



mahasiswa1 = MahasiswaKelas("PBO", "Ronaldo", 66, "Asep knalpot", "1103223048", 80, 85, 90)
mahasiswa1.tampilkan_info()
"""
"""
def main():
    
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")

    angka_terakhir = int(nim[-3:])

    if angka_terakhir % 2 == 1:
        print("tugas No.1")
    else:
        print("tugas No.2")

    if int(nim[-2]) % 2 == 1:
        print("tugas No.3")
    else:
        print("tugas No.4")

    if int(nim[-1]) % 2 == 1:
        print("tugas No.5")
    else:
        print("tugas No.6")
    return "done"    

hasil = main()
print(hasil)
"""
"""
class Mahasiswa:
    def __init__(self, kelas, jumlah_mahasiswa):
        self.kelas = kelas
        self.jumlah_mahasiswa = jumlah_mahasiswa

class MahasiswaKelas(Mahasiswa):
    def __init__(self, kelas, jumlah_mahasiswa, nama, nim, clo1, clo2, clo3):
        super().__init__(kelas, jumlah_mahasiswa)
        self.nama = nama
        self.nim = nim
        self.clo1 = clo1
        self.clo2 = clo2
        self.clo3 = clo3

    def __mahasiswa_nilai(self):
        nilai_akhir = 0.35 * self.clo1 + 0.30 * self.clo2 + 0.35 * self.clo3
        return nilai_akhir

    def tampilkan_nilai_akhir(self):
        nilai_akhir = self.__mahasiswa_nilai()
        print(f"Nilai Akhir {self.nama} ({self.nim}) adalah: {nilai_akhir}")


result = MahasiswaKelas("PBO", 40, "Jaka Kelana", "1103223048", 80, 90, 75)
result.tampilkan_nilai_akhir()
print(f"Kelas: {result.kelas}")
print(f"Jumlah Mahasiswa: {result.jumlah_mahasiswa}")
"""
"""
class Student:
    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk

    def display_data(self):
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("IPK:", self.ipk)

    def search_data(self, nim):
        if self.nim == nim:
            return self
        else:
            return None

    def delete_data(self, nim):
        if self.nim == nim:
            del self
            print("Data mahasiswa dengan NIM", nim, "telah dihapus")
        else:
            print("Data mahasiswa dengan NIM", nim, "tidak ditemukan")

    def update_data(self, nim, new_nama, new_nim, new_ipk):
        if self.nim == nim:
            self.nama = new_nama
            self.nim = new_nim
            self.ipk = new_ipk
            print("Data mahasiswa berhasil diupdate")
        else:
            print("Data mahasiswa dengan NIM", nim, "tidak ditemukan")


students = []


def add_student():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    ipk = float(input("Masukkan IPK mahasiswa: "))
    student = Student(nama, nim, ipk)
    students.append(student)
    print("Data mahasiswa berhasil ditambahkan")


def display_students():
    if not students:
        print("Belum ada data mahasiswa")
    else:
        for student in students:
            student.display_data()


def search_student():
    nim = input("Masukkan NIM mahasiswa yang ingin dicari: ")
    for student in students:
        result = student.search_data(nim)
        if result:
            result.display_data()
            break
    else:
        print("Data mahasiswa dengan NIM", nim, "tidak ditemukan")


def delete_student():
    nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
    for student in students:
        result = student.search_data(nim)
        if result:
            students.remove(result)
            print("Data mahasiswa dengan NIM", nim, "telah dihapus")
            break
    else:
        print("Data mahasiswa dengan NIM", nim, "tidak ditemukan")


def update_student():
    nim = input("Masukkan NIM mahasiswa yang ingin diupdate: ")
    for student in students:
        result = student.search_data(nim)
        if result:
            new_nama = input("Masukkan nama baru: ")
            new_nim = input("Masukkan NIM baru: ")
            new_ipk = float(input("Masukkan IPK baru: "))
            student.update_data(nim, new_nama, new_nim, new_ipk)
            break
    else:
        print("Data mahasiswa dengan NIM", nim, "tidak ditemukan")


while True:
    print("\nMenu:")
    print("1. Tambah data mahasiswa")
    print("2. Tampilkan data mahasiswa")
    print("3. Cari data mahasiswa")
    print("4. Hapus data mahasiswa")
    print("5. Update data mahasiswa")
    print("6. Keluar")

    pilih = input("Masukkan pilihan : ")

    if pilih == "1":
        add_student()
    elif pilih == "2":
        display_students()
    elif pilih == "3":
        search_student()
    elif pilih == "4":
        delete_student()
    elif pilih == "5":
        update_student()
    elif pilih == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid")

"""

#Web scrapping 

#fungsi request
"""
import requests
req = requests.get("https://id.wikipedia.org/wiki/Cristiano_Ronaldo")
from logging import info
print(req)

#inisialisasi beuatifulsoup
from bs4 import BeautifulSoup as bs
soup = bs(req.content,"html.parser")

print(soup)

#metode find(tag,attrs)
paragraft = soup.find("h2")
for x in paragraft:
    print(x,end="\n\n") 
#find all 
paragraft = soup.find_all("p")
for x in paragraft:
    print(x,end="\n")     

#get_text
paragraft = soup.find_all("p")
for x in paragraft:
    print(x.get_text(),end="\n\n") 

soup = bs(req.content,"html.parser")
print(soup.find("h1",{"id":"firstHeading"}).text)

#mengolah data
import requests
from bs4 import BeautifulSoup as bs
from logging import info

req = requests.get("https://id.wikipedia.org/wiki/Cristiano_Ronaldo")
info(req)

# Inisialisasi BeautifulSoup
soup = bs(req.content, "html.parser")

# Pilih infobox dengan class yang sesuai
infobox = soup.find("table", {"class": "infobox"})

# Cek apakah infobox ditemukan
if infobox:
    data = infobox.find("tbody")
    data = data.find_all("tr")

    informasi = {}

    for indata in data[2:]:
        try:
            judul = indata.find('th').get_text()
            info = indata.find('td').get_text()
        except:
            pass
        else:
            informasi[judul] = info

    for key in informasi:
        print(key, "=", informasi[key])
else:
    print("Invalid")
"""
"""
import requests
from bs4 import BeautifulSoup as bs
req = requests.get("https://id.wikipedia.org/wiki/Bruce_Lee")
soup = bs(req.content,"html.parser")
#print(soup)
#paragraft = soup.find_all("p")
#print(paragraft)
#for x in paragraft:
#    print(x.get_text(),end="\n\n") 
#print(soup.find("h1",{"id":"firstHeading"}).text)
infobox = soup.find('table',{'class' : 'infobox biography vcard'})
data = infobox.find_all('tr')

informasi = {}
for data in data[2:]:
    judul = data.find('th').get_text().replace('\xa0',' ')
    info = data.find('td').get_text().replace('\xa0',' ')
    informasi[judul]=info
print(informasi) 
    
"""
"""
from tabulate import tabulate
from abc import ABC, abstractmethod
import datetime

class Vehicle(ABC):
    def __init__(self, vehicle_number, vehicle_type, vehicle_name, owner_name):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.vehicle_name = vehicle_name
        self.owner_name = owner_name
        self.date = datetime.datetime.now().strftime('%d-%m-%Y')
        self.time = datetime.datetime.now().strftime('%H:%M:%S')

    @abstractmethod
    def calculate_charge(self, hours):
        pass

class Bicycle(Vehicle):
    def calculate_charge(self, hours):
        return 2000 * hours

class Bike(Vehicle):
    def calculate_charge(self, hours):
        return 4000 * hours

class Car(Vehicle):
    def calculate_charge(self, hours):
        return 6000 * hours

class ParkingManagement:
    def __init__(self):
        self.vehicles = []

    def vehicle_entry(self, vehicle):
        self.vehicles.append(vehicle)
        print("\n............................................................Record detail saved..................................................................")

    def remove_entry(self, vehicle_number):
        for vehicle in self.vehicles:
            if vehicle.vehicle_number == vehicle_number:
                self.vehicles.remove(vehicle)
                print("\n............................................................Removed Successfully..................................................................")
                break
        else:
            print("No Such Entry")

    def view_parked_vehicle(self):
        count = 0
        print("----------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\tParked Vehicle")
        print("----------------------------------------------------------------------------------------------------------------------")
        headers = ["Vehicle No.", "Vehicle Type", "Vehicle Name", "Owner Name", "Date", "Time"]
        rows = [[v.vehicle_number, v.vehicle_type, v.vehicle_name, v.owner_name, v.date, v.time] for v in self.vehicles]
        print(tabulate(rows, headers, tablefmt="fancy_grid"))
        count = len(self.vehicles)
        print("----------------------------------------------------------------------------------------------------------------------")
        print("------------------------------------------ Total Records - ", count, "-------------------------------------------------------")
        print("----------------------------------------------------------------------------------------------------------------------")

    def view_left_parking_space(self, bicycles, bikes, cars):
        print("----------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\tSpaces Left For Parking")
        print("----------------------------------------------------------------------------------------------------------------------")
        available_bicycles = sum(1 for v in self.vehicles if isinstance(v, Bicycle))
        available_bikes = sum(1 for v in self.vehicles if isinstance(v, Bike))
        available_cars = sum(1 for v in self.vehicles if isinstance(v, Car))
        table_data = [
            ["Spaces Available for Bicycle", bicycles - available_bicycles],
            ["Spaces Available for Bike", bikes - available_bikes],
            ["Spaces Available for Car", cars - available_cars]
        ]
        print(tabulate(table_data, tablefmt="fancy_grid"))
        print("----------------------------------------------------------------------------------------------------------------------")

    def generate_bill(self, vehicle_number, hours):
        for vehicle in self.vehicles:
            if vehicle.vehicle_number == vehicle_number:
                charge = vehicle.calculate_charge(hours)
                additional_charge = 0.18 * charge
                total_charge = charge + additional_charge
                print("\tVehicle Check-in time - ", vehicle.time)
                print("\tVehicle Check-in Date - ", vehicle.date)
                print("\tVehicle Type - ", vehicle.vehicle_type)
                table_data = [
                    ["Parking Charge", charge],
                    ["Additional charge 18%", additional_charge],
                    ["Total Charge", total_charge]
                ]
                print(tabulate(table_data, tablefmt="fancy_grid"))
                print("..............................................................Thank you for using our service...........................................................................")
                input("\tPress Any Key to Proceed - ")
                break
        else:
            print("No Such Entry")

def main():
    parking_management = ParkingManagement()
    bicycles = 78
    bikes = 100
    cars = 250

    while True:
        print("----------------------------------------------------------------------------------------")
        print("\t\tParking Management System")
        print("----------------------------------------------------------------------------------------")
        print("1.Vehicle Entry")
        print("2.Remove Entry")
        print("3.View Parked Vehicle ")
        print("4.View Left Parking Space ")
        print("5.Amount Details ")
        print("6.Bill")
        print("7.Close Program ")
        print("+---------------------------------------------+")
        ch = int(input("\tSelect option:"))

        if ch == 1:
            vehicle_number = input("\tEnter vehicle number (XXXX-XX-XXXX) - ").upper()
            vehicle_type = input("\tEnter vehicle type(Bicycle=A/Bike=B/Car=C):").lower()
            vehicle_name = input("\tEnter vehicle name - ")
            owner_name = input("\tEnter owner name - ")

            if vehicle_type == 'a':
                vehicle = Bicycle(vehicle_number, "Bicycle", vehicle_name, owner_name)
            elif vehicle_type == 'b':
                vehicle = Bike(vehicle_number, "Bike", vehicle_name, owner_name)
            elif vehicle_type == 'c':
                vehicle = Car(vehicle_number, "Car", vehicle_name, owner_name)
            else:
                print("Invalid vehicle type")
                continue

            parking_management.vehicle_entry(vehicle)

        elif ch == 2:
            vehicle_number = input("\tEnter vehicle number to Delete(XXXX-XX-XXXX) - ").upper()
            parking_management.remove_entry(vehicle_number)

        elif ch == 3:
            parking_management.view_parked_vehicle()

        elif ch == 4:
             parking_management.view_left_parking_space(bicycles, bikes, cars)

        elif ch == 5:
            print("----------------------------------------------------------------------------------------------------------------------")
            print("\t\t\t\tParking Rate")
            print("----------------------------------------------------------------------------------------------------------------------")
            print("*1.Bicycle      Rp2000 / Hour")
            print("*2.Bike         Rp4000/ Hour")
            print("*3.Car          Rp6000/ Hour")
            print("----------------------------------------------------------------------------------------------------------------------")

        elif ch == 6:
            vehicle_number = input("\tEnter vehicle number to Delete(XXXX-XX-XXXX) - ").upper()
            hours = int(input("\tEnter No. of Hours Vehicle Parked - "))
            parking_management.generate_bill(vehicle_number, hours)

        elif ch == 7:
            print("..............................................................Thank you for using our service...........................................................................")
            print("                                     **********(: Bye Bye :)**********")
            break

if __name__ == "__main__":
    main()

"""
"""
import numpy as np
import matplotlib.pyplot as plt

xn1 = [1, 1, 0, 3, 2, 2, 3, 0, 4, 8]  # sinyal impuls x1(n)
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # batas sinyal xn

plt.subplot(1, 2, 1)
plt.stem(n, xn1)  # untuk menampilkan sinyal diskrit
plt.xlabel("waktu diskrit")  # memberi nama pada sumbu x
plt.ylabel("x1(n)")  # memberi nama pada sumbu y
plt.title("Sinyal Diskrit x1(n)")  # memberi nama pada figure
plt.xticks(np.arange(0, 10, 1))  # menetapkan label pada sumbu x
plt.grid()
plt.tight_layout()
plt.show()

"""
"""
import numpy as np
import matplotlib.pyplot as plt

level = 1
sampling_rate = 16
sampling_period = 1 / sampling_rate
vd = np.arange(0, 2, sampling_period)
vdelta = np.zeros(level)
for i in range(level):
    vdelta[i] = (vd[i] + vd[i + 1]) / 2

samples = 50
t = np.arange(1, samples + 1)
x = 5 * np.cos(2 * np.pi * (10000 / 500000) * t)  # sinyal input, menggantikan nilai fm/fs
i = np.arange(0, level)
binary = [format(x, '03b') for x in i]  # decimal to binary conversion

for i in range(samples):
    for j in range(level):
        if x[i] < vd[1]:
            x[i] = vdelta[0]
        elif x[i] > vd[-1]:
            x[i] = vdelta[-1]
        elif x[i] <= vd[j + 1] and x[i] >= vd[j]:
            x[i] = vdelta[j]

plt.plot(t, x)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Quantized Signal')
plt.grid(True)
plt.show()
"""
"""
from sympy import symbols, Sum, oo, simplify, Function

# Fungsi untuk menghitung transformasi Z
def z_transform(signal):
    n, z = symbols('n z')
    x_n = signal

    # Transformasi Z dari u(n)
    u_n_transform = 1 / (1 - 1/z)

    # Transformasi Z dari x(n)
    x_n_transform = Sum(x_n * z**(-n), (n, 0, oo)).doit()

    # Simplifikasi ekspresi
    x_n_transform_simplified = simplify(x_n_transform)

    return x_n_transform_simplified

# Sinyal linier: x(n) = u(n) + 0.7n * u(n)
x_n = 1 + 48 * symbols('n')  # x(n) = u(n) + 0.7n * u(n)

# Hitung transformasi Z
transformed_signal = z_transform(x_n)

# Tampilkan sintaks dan output
print(f"x(n) = {x_n}")
print(f"Transformasi Z dari x(n) = {transformed_signal}")
"""

import matplotlib.pyplot as plt
import numpy as np

# Contoh data akses halaman (ini harus diganti dengan data nyata Anda)
# Anggap ini adalah timestamps (waktu) ketika halaman diakses
timestamps = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Anggap ini adalah nomor halaman yang diakses pada waktu tersebut
page_numbers = np.array([1, 2, 3, 2, 1, 2, 3, 4, 5, 3])

# Buat plot
plt.figure(figsize=(10, 6))  # Ukuran plot dalam inci
plt.scatter(timestamps, page_numbers, color='blue')  # Buat scatter plot

# Memberi label pada sumbu x dan y
plt.xlabel('Waktu')
plt.ylabel('Nomor Halaman')

# Menambahkan judul
plt.title('Akses Halaman Seiring Waktu')

# Menampilkan garis grid
plt.grid(True)

# Menampilkan plot
plt.show()




