a=1
max=0
while a!=0:
    if a>max:
        max=a
    a=int(input("Masukan bilangan : "))
    if a==0:
        break
print ("Nilai terbesarnya adalah :",max)
