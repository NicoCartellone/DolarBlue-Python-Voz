import requests
import msvcrt
from typing import Text
import pyttsx3


url = 'https://api-dolar-argentina.herokuapp.com/api/dolarblue'

r = requests.get(url)

datos = r.json()

compra = datos['compra']
venta = datos['venta']
fecha = datos['fecha']

print("Dolar Blue: compra: {}, venta: {}, fecha: {}".format(compra, venta, fecha))

engine = pyttsx3.init()
engine.setProperty("rate", 140)
Text = "Dolar Blue: compra: {}, venta: {}, fecha: {}".format(
    compra, venta, fecha)
engine.say(Text)
engine.runAndWait()

char = msvcrt.getche()
