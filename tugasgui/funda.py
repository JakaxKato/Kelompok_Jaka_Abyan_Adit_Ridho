#IF ELSE statement
"""
nilai = int(input("nilai mtk : "))

if nilai > 70:
    print("oke aman")

else: 
    print("remed wak")
print(f"penliaian selesai  {nilai}")
"""
#El If statement
"""
nama = input("nama : ")

if nama == "sule" :
    print("sia saha")
elif nama == "asep":
    print("betul mang")
else:
    print("teu wauh")
print("ges beres")
"""
"""
#latihan percabangan
# kalkulator 
print(25*"=")
print("Kalkulator gacor")
print(25*"=" + "\n")

angka_1 = float(input("masukkan angka 1 = "))
operator = input("masukkan operator (+,-,*,/)")
angka_2 = float(input("masukkan angka 2 = "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasil nya = {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasil nya = {hasil} ")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya = {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya = {hasil}")
else:
    print("masukin yg bener bang")
print("selesai")
"""

#perulangan  for loop 
# dengn list
"""
angka = [0,1,2,3,4]
for i in angka:
    print(f"i sekarang --> {i}")
print('done \n')

# dengan range
angka2 = range(5)

for i in range(1,5) :
    print("*")
print("done \n")

# str
data_str = "jaka kelana"

for i in data_str:
    print(i)
print('done ')
"""
#while loop
"""
angka = 1
print(f"angka ayena -> {angka} \n")

while angka < 5 :
    angka += 1
    print(f"angka ayena -> {angka}")
    print("lanjutkaan")

print("done")
"""
# Continue and Pass and Break
# Continue
"""
angka = 1
print(f"angka ayena -> {angka} \n")

while angka < 5 :
    angka += 1
    print(f"angka ayena -> {angka}")
    if angka == 3 :
        continue
    print("lanjutkaan")

print("done")
"""
"""
# break
angka = 1
print(f"angka ayena -> {angka} \n")

while angka < 5 :
    angka += 1
    print(f"angka ayena -> {angka}")
    if angka == 3 :
        break
    print("lanjutkaan")

print("done")

data_nilai = int(input("hitung sampai = "))

angka = 0

while True:
    angka +=1
    print(f"angka sekrang -> {angka}")
   
    if angka == data_nilai:
        print("teruskan")
        break
    print("wasap")
    
print("done")
"""
#Latihan Perulangan

#menggunakan for 
sisi = 5
print("Awal for")
count = 1
for i in range (sisi):
    print("*"*count)
    count += 1

print("akhir for \n")
# Menggunakan While
print("awal while")

count = 1
while True:
    print("*"*count)
    count +=1
    if count == sisi:
        break

print("akhir while \n")