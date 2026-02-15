#MENGKONVERSI TEMPERATUR SUHU

#Celcius ke Temperatur lain
print ("=======Celcius ke Temperatur lain=======")

celcius = 5
print ("Jika suhu celciusnya adalah", celcius, "C")

#1. Celcius ke Reamur
celcius = 5
keReamur = (4/5) * celcius #ini adalah rumusnya
print ("Reamurnya adalah",keReamur, "R")

#2. Celcius ke Farenheit
celcius = 5
keFarenheit = ((9/5) * celcius) + 32 #ini adalah rumusnya
print ("Farenheitnya adalah", keFarenheit, "F")

#3. Celcius ke Kelvin
celcius = 5
keKelvin = celcius + 273 #ini adalah rumusnya
print ("Kelvinnya adalah", keKelvin, "K")

#Reamur ke Temperatur lain
print ("=======Reamur ke Temperatur lain=======")

reamur = 5
print ("Jika suhu reamurnya adalah", reamur, "R")

#1 Reamur ke Celcius
reamur = 5
keCelcius = ((5/4) * reamur)
print ("Celsiusnya adalah", keCelcius, "C")

#2 Reamur ke Farenheit
reamur = 5
keFarenheit = ((9/4) * reamur) + 32
print ("Farenheitnya adalah", keFarenheit, "F")

#3 Reamur ke Kelvin
reamur = 5
keKelvin = ((5/4) * reamur) + 273
print ("Kelvinnya adalah", keKelvin, "K")

#Farenheit ke Temperatur lain
print ("=======Farenheit ke Temperatur lain=======")

farenheit = 5
print ("Jika suhu farenheitnya adalah", farenheit, "F")

#1. Farenheit ke Celcius
farenheit = 5
keCelcius = 5/9 * (farenheit - 32)
print ("suhu celsiusnya adalah", keCelcius, "C")

#2. Farenheit ke Reamur
farenheit = 5
keReamur = 4/9 * (farenheit - 32)
print ("suhu reamurnya adalah", keReamur, "R")

#3. Farenheit ke Kelvin
farenheit = 5
keKelvin = 5/9 * (farenheit - 32) + 273
print ("suhu kelvinnya adalah", keKelvin, "K")

#Kelvin ke Temperatur lain
print ("=======Kelvin ke Temperatur lain=======")

#1. Kelvin ke Celcius
kelvin = 5
keCelcius = kelvin - 273
print ("suhu celciusnya adalah", keCelcius, "C")

#2. Kelvin ke Reamur
kelvin = 5
keReamur = 4/5 * (kelvin - 273)
print ("suhu reamurnya adalah", keReamur, "R")

#3. Kelvin ke Farenheit
kelvin = 5
keFarenheit = 9/5 * (kelvin - 273) + 32
print ("suhu farenheitnya adalah", keFarenheit, "F")