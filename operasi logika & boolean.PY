#OPERASI LOGIKA

print ("=====NOT=====")
a = True
b = not a       #tambahkan not
print ('data a =', a)  
print ('data b =', b)
#Output False, karena data b bukanlah data a

c = False
d = not c
print ('data c =', c)  
print ('data d =', d)


print ("=====OR=====")
#Jika dua data salah satunya bernilai true, maka outputnya akan true

a = True
b = False
c = a or b
print ('true (a)', 'OR', 'false(b) =', c) #outputnya true

a = False
b = True
c = a or b
print ('true (a)', 'OR', 'false(b) =', c) #outputnya true

a = True
b = True
c = a or b
print ('true (a)', 'OR', 'false(b) =', c) #outputnya true

a = False
b = False
c = a or b
print ('true (a)', 'OR', 'false(b) =', c) #outputnya false


print ("=====AND=====")
#Jika dua data salah satunya bernilai false, maka outputnya akan false

a = True
b = False
c = a and b
print ('true (a)', 'AND', 'false(b) =', c) #outputnya false

a = False
b = True
c = a and b
print ('false(a)', 'AND', 'true (b) =', c) #outputnya false

a = False
b = False
c = a and b
print ('false(a)', 'AND', 'false(b) =', c) #outputnya false

a = True
b = True
c = a and b
print ('true (a)', 'AND', 'true (b) =', c) #outputnya true

print ("=====XOR=====")
#Jika dua data salah satunya bernilai true, maka outputnya akan true

a = True
b = False
c = a ^ b
print ('true (a)', 'XOR', 'false(b) =', c) #outputnya true

a = False
b = True
c = a ^  b
print ('false(a)', 'XOR', 'true (b) =', c) #outputnya true

a = False
b = False
c = a ^  b
print ('false(a)', 'XOR', 'false(b) =', c) #outputnya false

a = True
b = True
c = a ^ b
print ('true (a)', 'XOR', 'true (b) =', c) #outputnya false