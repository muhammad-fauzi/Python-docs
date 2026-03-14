#OPERASI BINERY
"""Adalah operasi yang fokus pada binery
sebuah angka dalam variabel"""

a = 5
print (a, 'binery nya adalah =', format (a,'08b')) #o8b adalah format penulisan binery
#binery dari 5 adalah 00000101

#sekarang mengoperasikan antar binery
print ("=======OPERASI 'OR' PADA BINERY=======")

#1. menggunakan OR (|)
x = 3
y = 6

z = x | y
print(x, 'binery nya adalah =', format(x, '08b'))
print(y, 'binery nya adalah =', format(y, '08b'))
print('------------------------------ (|)')
print(z, 'binery hasilnya =', format(z, '08b')) #outputnya 00000111 (binery 7)
#jadi, hasil operasi ditentukan dari binery nya
#angka 1 pada binery dianggap true
#angka 0 pada binery dianggap false

print ("======OPERASI 'AND' PADA BINERY=======")
#2. menggunakan AND (&)

d = 7
e = 8

f = 7 & 8
print (d, 'binery nya adalah =', format (d, '08b'))
print (e, 'binery nya adalah =', format (e, '08b'))
print('------------------------------ (&)')
print (f,'binery nya adalah =', format (f, '08b')) 
#outputnya 00000000 (binery 0)

print ("======OPERASI 'XOR' PADA BINERY=======")
#3. menggunakan XOR (^)

g = 2
h = 5

i = 2 ^ 8
print (g, 'binery nya adalah =', format (g, '08b'))
print (h, 'binery nya adalah =', format (h, '08b'))
print('------------------------------ (^)')
print (i,'binery nya adalah =', format (i, '08b'))
#outputnya 00001010  (binery 10)

print ("======OPERASI 'NOT' PADA BINERY=======")
#4. menggunakan NOT (~) #ini adalah mirroring / kebalikan + 1

i = 3
j = ~i
print (i, 'binery nya adalah =', format(i, '08b'))
print (j, 'binery nya adalah =', format(j, '08b')) 
#outputnya -4

k = 0b00000101
l = 0b11111111

print ('nilai KL =', k^l, ', binery =', format (k^l, '08b'))
#output nilai KL = 250 , binery = 11111010 

print ("===OPERASI 'SHIFTING' PADA BINERY====")
# Shifting ialah menggeser angka 1 pada binery ke kanan maupun ke kiri 
# angka 1 yang digeser ialah angka yang berada di tengah. 

print ("===SHIFTING KANAN====")

#5. menggunakan SHIFT (>>) ke kanan

m = 7
print (m, 'binery nya adalah = ', format (m, '08b')) # binerynya 00000111

n = m >> 1 #menggeser 1 angka ke kanan
print (n, 'binery nya adalah = ', format (n, '08b')) 
#outputnya biner 00000011 (yaitu angka 3)

print ("===SHIFTING KIRI====")
#6. menggunakan SHIFT (<<) ke kiri

o = 8
print (o, 'binery nya adalah = ', format (o, '08b')) # binerynya 00001000

p = o << 3 #menggeser 3 angka ke kiri
print (p, 'binery nya adalah = ', format (p, '08b')) 
#outputnya biner 01000000 (yaitu angka 64)