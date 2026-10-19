"""Respuesta = input("¿has una pregunta sobre lo que quieras y sera contestada?")
Respuesta = "si"
print(Respuesta)"""

#Esta fue otra prueba de como hacer que la gran ia conteste a preguntas de si o no, pero con un porcentaje de probabilidad de 90% para que diga si y 10% para que diga no.
input("¿Haz una pregunta de si o no a la gran ia?")

import random

opciones = ["Sí", "No"]
# Definimos los porcentajes de probabilidad para cada opción en orden
porcentajes = [50, 50]

# random.choices devuelve una lista, por lo que usamos [0] para sacar el resultado
resultado = random.choices(opciones, weights=porcentajes, k=1)[0]
print(resultado)
