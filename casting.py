#   CASTING DATA
"""Casting data adalah merubah suatu tipe data ke tipe data yang lain
    contoh"""

# CASTING DARI INTEGER KE TIPE DATA LAIN
print ("===========UBAH TIPE DATA DARI INTEGER==========")
casting1_int = 5 #tipe INTEGER
print ("integer:", casting1_int, ", type: ", type(casting1_int))

    #1. ubah dari integer ke float
casting1_float = float (casting1_int)
print ("contoh int_ke_float= ", casting1_float,", type=", type(casting1_float))
# output berubah, dari 5 (int) menjadi 5.0 (float)

    #2. ubah dari integer ke string
casting1_str = str (casting1_int)
print ("contoh int_ke_str: ", casting1_str, ", type: ", type(casting1_str))

    #3. ubah dari integer ke boolean
casting1_bool = bool (casting1_int)
print ("contoh int_ke_bool: ", casting1_bool, ", type: ", type(casting1_bool))
#jika casting_int nilainnya selain 0 outputnya selalu true. jika 0, maka false

# CASTING DARI FLOAT KE TIPE DATA LAIN
print ("===========UBAH TIPE DATA DARI FLOAT==========")
casting2_float = 5.7 #tipe FLOAT
print ("float:", casting2_float, ", type: ", type(casting2_float))

    #1. ubah dari float ke integer
casting2_int = int (casting2_float)
print ("contoh float_ke_int= ", casting2_int,", type=", type(casting2_int))
#outputnya 5, nilai 5.7 (float) akan dibulatkan ke bawah saat berubah jadi int

    #2. ubah dari float ke string
casting2_str = str (casting2_float)
print ("contoh float_ke_str: ", casting2_str, ", type: ", type(casting2_str))

    #3. ubah dari float ke boolean
casting2_bool = bool (casting2_float)
print ("contoh float_ke_bool: ", casting2_bool, ", type: ", type(casting2_bool))
#jika casting_float nilainnya selain 0 outputnya selalu true. jika 0, maka false

#CASTING DARI STRING KE TIPE DATA LAIN
print ("===========UBAH TIPE DATA DARI STRING==========")
casting3_string = "" #tipe STRING
print ("string:", casting3_string, ", type: ", type(casting3_string))

    #1. ubah dari string ke integer
casting3_int = int (casting3_string)
print ("contoh string_ke_int= ", casting3_int,", type=", type(casting3_int))
#jika casting_string nilainya berupa karakter/huruf, outputnya akan error 

    #2. ubah dari string ke float
casting3_float = float (casting3_string)
print ("contoh str_ke_float: ", casting3_float, ", type: ", type(casting3_float))
#jika casting_stringnya berupa desimal, output floatnya akan error

    #3. ubah dari string ke boolean
casting3_bool = bool (casting3_string)
print ("contoh string_ke_bool: ", casting3_bool, ", type: ", type(casting3_bool))
#jika casting_string nilainnya berupa angka, outputnya true. 
#jika casting_string nilainya "True", outputnya true
#jika casting_string nilainya "False", outputnya false
"""jika casting_string nilainya "" (kosong), outputnya akan false,
dengan catatan contoh casting3 int, float harus dimatikan dulu
untuk pembuktiannya"""

#CASTING DARI BOOLEAN KE TIPE DATA LAIN
print ("===========UBAH TIPE DATA DARI BOOLEAN==========")
casting4_bool = False #tipe bool
print ("bool:", casting4_bool, ", type: ", type(casting4_bool))

   #1. ubah dari bool ke integer
casting4_int = int (casting4_bool)
print ("contoh bool_ke_int= ", casting4_int,", type=", type(casting4_int))
#Data bool "true" diubah ke integer jadi 1, kalo "false" jadi 0

    #2. ubah dari bool ke float
casting4_float = float (casting4_bool)
print ("contoh bool_ke_float: ", casting4_float, ", type: ", type(casting4_float))
#Data bool "true" diubah ke float jadi 1.0, kalo "false" jadi 0.0

    #3. ubah dari bool ke string
casting4_string = str (casting4_bool)
print ("contoh bool_ke_string: ", casting4_string, ", type: ", type(casting4_string))
#Data bool "true" diubah ke string jadi True (text), kalo "false" jadi False (text)
