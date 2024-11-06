

from operator import truediv
import random


numero_secreto = random.randint(1,100)
cant_intentos = 0
cant_max_intentos = 10
adivinado = False

print("Bienvenido al juego de adivinar el número secreto!!")

while not adivinado:
    if not cant_intentos < cant_max_intentos:
        print("¡Game Over! No has podido adivinar dentro de los 10 intentos")
        break

    entrada = input("Introduce un número del 1 al 99: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("Felicitaciones!! Has adivinado el número secreto!")
        adivinado = True
    elif numero < numero_secreto:
        print("Mmmm, el número es mayor al ingresado")
    else:
        print("Uff, el número es menor al ingresado")

    cant_intentos += 1

