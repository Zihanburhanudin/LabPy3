# LabPy3
# Latihan1 (menampilkan n bilangan acak yang lebih kecil dari 0.5)
1. Alurnya :
-import random memanggil file random
-n = int(input("Masukan nilai N : ")) input variabel n, tipe data integer
-for i in range(n) : looping for, dengan jumlah perulangan sebanyak n
-a=random.uniform(0.0,0.5) variabel a berisikan random angka dari 0.0 sampai 0.5
-print ("data ke : ", i, "=> ", a) print data ke : i = index looping a = angka random sesuai syarat nomer 4
-print("Selesai") print Selesai di luar looping
-Tampilkan hasil kelayar

2. Algoritmanya :
import random

n = int(input("Masukan nilai N : "))
for i in range(n):
    a=random.uniform(0.0,0.5)
    print ("Data ke : ", i, "=> ", a)
print("Selesai")

# Latihan2 (menampilkan bilangan terbesar dari n buah data yang diinputkan)
1. Alurnya :
-a=1 //variable a diisi 1, agar bisa masuk ke syarat while max=0 //variable max diisi 0
-while a!=0 : looping while dengan syarat a bukan 0
-if x > max : max = a proses if untuk mencari nilai terbesar
-a = int(input("Masukan bilangan : ")) input nilai a dengan tipe data integer
-if a == 0 : break jika inputan a diisi angka 0 maka break alias berhenti looping
-print("Bilangan terbesar adalah : ",max) print nilai terbesar, variabel max

2. Algoritmanya :
a=1
max=0
while a!=0:
    if a>max:
        max=a
    a=int(input("Masukan bilangan : "))
    if a==0:
        break
print ("Nilai terbesarnya adalah :",max)

# Program1 (program sederhana perulangan)
1. Alurnya :
-x=100000000 modal 100,000,000, variable x
-sum=0 variable untuk menjumlah total laba
-y=0 variable untuk masa bulan
-lb = [int(0), int(0), int(x) * .1, int(x) * .1, int(x) * .5, int(x) * .5, int(x) * .5, int(x) * .2] 
*variable untuk jumlah laba perbulan, 
 dipisahkan dengan koma, tipe data integer
-for i in lb : looping for indexs i, dengan mengambil data dari lb
-sum=sum+i rumus untuk menghitung total laba perbulan
-y+=1 masa bulan, tiap looping menambah 1
-print("laba bulan ke-", y ,"sebesar :", i ) print : y = ambil masa bulan, i = ambil dari data yg ada di dalam lb
-print("Total laba adalah :", sum) print total laba
-Tampilkan hasil kelayar 

2. Algoritmanya :
x=100000000
sum=0
y=0
lb = [int(0), int(0), int(x) * .1, int(x) * .1, int(x) * .5, int(x) * .5,  int(x) * .5,  int(x) * .2]
print("Modal awal seorang pengusaha     :",x)
for i in lb :
    sum=sum+i
    y+=1
    print("Laba bulan ke-", y ,"sebesar :", i)
print("Total laba yang didapat adalah   :", sum)
