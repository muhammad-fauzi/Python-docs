#OPERASI KOMPARASI

"""
    Operasi Komparasi selalu menghasilkan Boolean
berikut adalah penanda assignmentnya

1. A lebih besar dari B (>)
2. A lebih kecil dari B (<)
3. A sama dengan / lebih besar dari B (>=)
4. A sama dengan / lebih kecil dari B (<=)
5. A sama dengan B (==)
6. A tidak sama dengan B (!=)
7. A adalah (is)
8. A bukanlah (is not)
"""

print ("====== Operasi Lebih Besar (>) ======")
#Contoh lebih besar (>)
a = 10
b = 5
hasil = a > b
print (a, '>', b, '=', hasil)

hasil = b > a
print (b, '>', a, '=', hasil)

hasil = 10 > a
print (a, '>', 10, '=', hasil)

print ("====== Operasi Lebih Kecil (<) ======")
#Contoh lebih kecil (<)
a = 5
b = 10
hasil = a < b
print (a, '<', b, '=', hasil)

hasil = 3 < a
print ('3', '<', a, '=', hasil)

hasil = 5 < a
print ('5', '<', a, '=', hasil)

print ("==== Operasi Sama dengan / Lebih Besar (>=) ====")
#Contoh sama dengan lebih besar (>)
a = 5
hasil = 5 >= 2
print (a, '>=', 2, '=', hasil) #output True

a = 2
hasil = 2 >= 2
print (a, '>=', 2, '=', hasil) #output True

a = 1
hasil = 1 >= 2
print (a, '>=', 2, '=', hasil) #output False

print ("==== Operasi Sama Dengan / Lebih Kecil (<=) ====")
#Contoh sama dengan lebih kecil (<)
a = 10
hasil = 10 <= 11
print (a, '<=', 11, '=', hasil) #True

a = 10
hasil = 10 <= 10
print (a, '<=', 10, '=', hasil) #True

a = 15
hasil = 15 <= 10
print (a, '<=',10 , '=', hasil) #False

print ("==== Operasi Sama Dengan (==) ====")
#Contoh sama dengan (==)
a = 3
hasil = a == 3
print (a, '==', '3', hasil) #True

hasil = a == 5
print (a, '==', '5', hasil) #False

print ("==== Operasi Tidak Sama Dengan (!=) ====")
#Contoh Tidak Sama Dengan (!=)
a = 5
hasil = a != 10
print (a, '!=', 10, hasil) #Output True karena 5 tidak sama dengan 10

hasil = a != 5
print (a, '!=', 5, hasil) #Output False karena 5 sama dengan 5

print ("==== Operasi is (is) ====")
"""Is adalah komparasi object identitiy yang mengindetifikasi
variabel. object yang dimaksud ialah variabel beserta nilainya, 
Contoh :
contohIs = 5"""

z = 5
print ('z =', z,', id=', hex(id(z)))
#140706387305720 ini adalah ID dari variabel z dan nilainya yang ditulis tanpa hex
#hex adalah hexadeximal, yaitu format penulisan basis 16
#jika ditulis dengan hex penulis ID menjadi 0x7ff8c23ba4f8
#perbedaan tersebut bukan masalah. hex hanya utk mempermudah cara baca
#untuk membuktikan ID 0x7ff8c23ba4f8 dan 140706387305720 adalah sama ialah
#Contonya
z = 5
print('z =',z, ', id=', id(z))
print(int(hex(id(z)), 16)) #Output 140706666423544
#16 menandakan bilangan bulat basis 16
#basis 16 adalah 0 1 2 3 4 5 6 7 8 9 a b c d e f
#kalo gak ditulis 16, python akan mengiranya sebagai desimal


"""Nah, Is pada python membandingkan ID tersebut. Kalo dua variabel
Id nya sama, outputnya akan true"""
x = 5
y = 5
hasilIs = x is y
print ('x = ', x, ', id= ', hex(id (x)))
print ('y = ', y, ', id= ', hex(id (y)))
print ('x = ', x, 'is', 'y =', y, hasilIs) #Outputnya True
"""True karena id nya sama. 
Id tsb diketahui dari nilai 2 variabel yg sama"""

a = 3
b = 5
hasilIs = a is b
print ('a = ', a, 'is', 'b =', b, hasilIs) #Outputnya False

#kalo perbandingan IS nya seperti ini,
a = 5
b = 5
hasilAB = a is 5 # A dibandingkan dengan literal 5
print ('a =', a, 'is', '5 =', hasilAB) 
""" akan muncul notif di atas seperti ini
is" with 'int' literal. Did you mean "=="?
hasilAB = a is 5
maksudnya ialah, agar perbandingan a is 5 sebaiknya pakai ==  
  """

print ("==== Operasi is not (is not) ====")
"""Is Not adalah komparasi kebalikan dari Is
Jika ID sebuah variabel sama dan dikomparasi dengan Is, outputnya true
Jika ID sebuah variabel berbeda dan dikomperasi dengan is not, outputnya true"""
k = 3
l = 5
hasilK = k is not l
print ('k = is not l', hasilK) #outputnya true, karena k dan l nilainya beda
#ceK id
print ('k =', k, 'id =',hex(id(k)))
print ('l =', l, 'id =',hex(id(l)))