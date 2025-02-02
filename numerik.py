import os, random
from scripts.myfunc import clear,f,persamaan

#--------------------------------------------------------------------------------------------------#
# Fungsi main
#--------------------------------------------------------------------------------------------------#
def hitung(persp):
    #var
    n = 0
    p = persamaan(persp)

    clear ()
    #pil[0] berisi pilihan metode pil[1] berisi string metode
    print("Metode Numerik")
    print("Persamaan, %s"%(persp))
    print()
    print("(Berapa angka dibelakang koma. Masukkan 2 jika tidak yakin)")
    rou = int(input("Pembulatan : "))
    print("(Ingin mendekati nilai berapa. Masukkan 0 jika tidak yakin)")
    err = float(input("Masukkan Error : "))

    while True:
        print()
        x1 = float(input("Masukkan X1 : "))
        x2 = float(input("Masukkan X2 : "))
        fx1 = round(f(x1,p),rou)
        fx2 = round(f(x2,p),rou)
        print()
        print("Nilai dari, F(%d) = %f " % (x1,fx1))
        print("Nilai dari, F(%d) = %f " % (x2,fx2))
        print()
        check = fx1*fx2
        if check < 0:
        	print("Syarat sudah ok. f(%d)*f(%d) < 0 || %5.2f < 0"%(x1,x2,check))
        	break
        else:
        	print("Syarat belum ok f(%d)*f(%d) >= 0 || %5.2f >= 0"%(x1,x2,check))

    print()
    #Mempersiapkan output berupa tabel
    print("X1 = %d , X2 = %d , Error = %.6f"% (x1,x2,err))
    print("_______________________________________________________")
    print("  n           x              f(x)             error    ")
    print("_______________________________________________________")

    #Hanya untuk initialisasi
    cektemp = random.randint(1,100)

    while True:
        #Counter Iterasi
        n = n + 1

        x3 = round(((x1 + x2)/2),rou)

        fx3 = round(f(x3,p),rou)

        #Output Sesuai bentuk tabel
        print("%3d|     %.8f       %10.8f      %12.10f" % (n,x3,fx3,fx3))

        #Print Akar Persamaan
        if abs(fx3) <= err or abs(fx3) == cektemp :
        	print("________________")
        	print("Akar Persamaan, %.36f"%(x3))
        	print("Atau ~ %.4f"%(round(x3,4)))
        	print("Error, %.4f"%(round(fx3,4)))
        	print()
        	print("Note!")
        	print("Saat Melakukan perhitungan pastikan gunakan pembulatan")
        	print("agar mendapatkan jawaban yang sesuai dengan taraf error")
        	break

        if f(x1,p) * f(x3,p) > 0:
        	x1 = x3
        else :
        	x2 = x3

        cektemp = abs(fx3)

        #Agar memudahkan pembacaan iterasi. setiap 10 iterasi di stop.
        if n%10 == 0:
        	input("Lanjut? Tekan enter.")
