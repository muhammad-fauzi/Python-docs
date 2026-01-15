# MENGAMBIL DATA DARI USER
"""Ialah memasukkan data secara langsung pada terminal
    dan menambahkan kata kunci "input"
    contoh"""

biodata = input ("Nama Lengkap: ")
print ("biodata =", biodata, "type:", type (biodata))

"""ouputnya "Nama Lengkap", dan bisa diisi angka/huruf di terminal.
Jika dipencet enter pada terminal, keluar keterangan 
tipe datanya, yaitu string"""

    #Jika ingin mengambil data berupa integer

umur = int (input("umur:")) #tambahkan keterangan int
print ("umur:", umur, "type:", type(umur))

"""outputnya "umur" dan hanya bisa diisi oleh angka di terminal dan 
akan bertipe integer. Jika dikosongkan atau diisi dengan 
angka dalam bentuk float (desimal) atau huruf, outputnya akan error"""

    #jika ingin mengambil data berupa float

tinggi = float (input("tinggi badan:")) #tambahkan keterangan float
print ("tinggi:", tinggi, "type:", type (tinggi))

"""outputnya "tinggi". jika diisi dengan angka, maka dibelakang angka
akan ditambahkan (.0) , contohnya: diisi 5, hasilnya 5.0 
dalam bentuk float"""

    #jika ingin mengambil data berupa boolean

lulus = bool (input("apakah dia lulus:"))
print("apakah dia lulus:", lulus,"type:", type(lulus))

"""jika outputnya diisi "true", angka atau huruf, maka ketika 
dipencet enter, hasilnya juga "true".

jika outputnya diisi "false", hasilnya juga akan "true".

Untuk menghasilkan "false", boolean harus diubah dulu ke integer"""

menang = bool (int(input("apakah dia menang:")))
print("apakah dia menang:", menang, "type:", type(menang))

"""output hanya bisa diisi dengan angka. jika diisi dengan 0, 
hasilnya akan "false". Tapi jika diisi dengan huruf atau angka float,
hasilnya akan eror"""