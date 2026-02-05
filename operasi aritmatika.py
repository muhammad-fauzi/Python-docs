# OPERASI ARITMATIKA

#1. Penjumlahan (+)
x = 8
y = 7
hasilA = x + y
print (x,'+', y, '=', hasilA) #Output dalam bentuk integer

#2. Pengurangan (-)
x = 8
y = 7
hasilB = x - y
print (x,'-', y, '=', hasilB) #Output dalam bentuk integer

#3. Perkalian (*)
x = 8
y = 7
hasilC = x * y
print (x,'*', y, '=', hasilC) #Output dalam bentuk integer

#4. Pembagian (/)
x = 8
y = 7
hasilD = x / y
print (x,'/', y, '=', hasilD) #Output dalam bentuk float

#5. Perpangkatan (eksponen) (**)
x = 10
y = 3
hasilE = x ** y
print (x,'**', y, '=', hasilE) #Output dalam bentuk integer

#6. Sisa pembagian (modulus) (%)
x = 10
y = 3
hasilF = x % y
print (x, '%', y, "=", hasilF) #Outputnya adalah 1
#jika tidak ada sisa pembagian (contoh x = 12), outputnya adalah 0

#7. Pembulatan (floor division) (//)
x = 8
y = 7
hasilG = x // y
print (x, '//', y, '=', hasilG)
#output sebelumnya 1.14285 sekian, sekarang dibulatkan ke bawah jadi 1

#8. Prioritas Operasi
"""urutan prioritas operasi adalah
1. operasi dalam tanda kurung ()
2. operasi eksponen
3. operasi pembagian
4. operasi perkalian (* / ** // %)
5. operasi pertambahan/pengurangan"""

x = 7
y = 3
z = 2
hasilH = x + y - (y - z) * y / z ** z  #(tambah, kurang, kali, bagi)
print (x, '+', y, '-', y, '-', 2, '*', y, '/', z, '**', z, '=', hasilH)
"""urutan operasinya
1. tanda kurung () (y-z)            => 3 - 2 = 1
2. pangkat (z**z)                   => 2 ** 2 = 4
3. pembagian (y / (z**z))           => 3 / 4 = 0.75
4. perkalian (y-z) * (y/z**z)       => 1 * 0.75 = 0.75 
5. tambah & kurang (x + y - 0.75)   => 7 + 3 - 0.75 = 9.25
"""
