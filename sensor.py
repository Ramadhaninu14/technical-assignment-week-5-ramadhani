#2Script sensor.py dan sebuah fungsi untuk mengambil data dari sensor tersebut

from gpiozero import LightSensor
ldr = LightSensor(4)
while True:
	print(ldr.value)
