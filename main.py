#3Sebuah script utama main.py yang terdiri dari sebuah logic sederhana yang menjawab sebuah use case sederhana 

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
delayt = .1 
value = 0 # variabel ini akan digunakan untuk menyimpan nilai ldr
ldr = 7 #ldr terhubung dengan pin nomor 7
led = 11 #led terhubung dengan pin nomor 11
GPIO.setup(led, GPIO.OUT) #karena led adalah perangkat output jadi itu sebabnya kami mengaturnya ke output.
GPIO.output(led, False) # tetap matikan secara default
def rc_time (ldr):
    count = 0
 
    #Output pada pin untuk
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, False)
    time.sleep(delayt)
 
    #Ubah pin kembali ke input
    GPIO.setup(ldr, GPIO.IN)
 
    #Hitung sampai pinnya tinggi
    while (GPIO.input(ldr) == 0):
        count += 1
 
    return count
 
 
#Tangkap saat skrip terganggu, bersihkan dengan benar
try:
    # Main loop
    while True:
        print("Ldr Value:")
        value = rc_time(ldr)
        print(value)
        if ( value <= 10000 ):
                print("Lights are ON")
                GPIO.output(led, True)
        if (value > 10000):
                print("Lights are OFF")
                GPIO.output(led, False)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()