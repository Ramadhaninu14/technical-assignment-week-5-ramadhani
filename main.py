#3Sebuah script utama main.py yang terdiri dari sebuah logic sederhana yang menjawab sebuah use case sederhana

from gpiozero import LightSensor
ldr = LightSensor(4)
while True:
	print(ldr.value)