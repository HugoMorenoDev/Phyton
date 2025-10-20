
import random
from faker import Faker
from funciones_ahorcado import getPalabra, transformaPalabra, compruebaLetra, compruebaEstado, compruebaIntentos
m = "hola";
print(m)
print("Bienvenido a juegos de Hugo")
selecciona_juego = int(input("Elije uno de los siguientes juegos escribiendo el número correspondiente" \
"\n 1- Adivina el número" \
"\n 2- Pedra - Paper -Tisores" \
"\n 3- El Penjat "  \
"\n 4- 3 en Raya "  \
"\n 5- BlackJack "  \
"\n 6- Hundir la flota \n"  \
"Número del juego: "))

#! JUEGO NÚMERO 1
if selecciona_juego == 1:
    print("Tienes que adivinar el número aleatorio entre el 1 y el 10")
    print("Tienes 3 intentos, si fallas los 3 pierdes")
    number = random.randint(1,10)
    #print("Número random es: ", number) #comentar esto al acabar
    print(number)
    first_try = int(input("Dime el primer número: "))

    if first_try > number:
        print("Es más pequeño del que buscamos")
    elif first_try < number:
        print("Es más grande del que buscamos")
    else:
        print("Felicidades, el número era:", number, "has GANADO")

    if first_try != number:
        print("No es el número:", first_try)
        second_try = int(input("Dime el segundo número: "))
        if second_try > number:
            print("Es más pequeño del que buscamos")
        elif second_try < number:
            print("Es más grande del que buscamos")
        else:
            print("Felicidades, el número era:", number, "has GANADO")

        if second_try != number:
            print("No es el número:", second_try)
            third_attempt = int(input("Dime el tercer y último número: "))
            if third_attempt == number:
                print("Felicidades, el número era:", number, "has GANADO")
            else:
                print("No es el número:", third_attempt)
                print("Has PERDIDO, el número era:", number)

#! JUEGO NÚMERO 2
elif selecciona_juego == 2:
    print("Tienes que sacar piedra, papel o tijera y juegas contra la máquina")

    posibilades = ["piedra","papel","tijera"]
    apuesta_pc = random.choice(posibilades)
    
    eleccion = input("Elije entre 'piedra', 'papel' o 'tijera'" \
    "\n¿Qué elijes?: ")
    mi_eleccion = eleccion.lower().strip()

    if mi_eleccion == "tijera" or mi_eleccion == "papel" or mi_eleccion == "piedra":
        if mi_eleccion == "piedra" and apuesta_pc == "papel":
            print("Has perido, la máquina ha sacado", apuesta_pc, "y tu", mi_eleccion)
        elif mi_eleccion == "piedra" and apuesta_pc == "tijera":
            print("Has ganado, la máquina ha sacado", apuesta_pc, "y tu", mi_eleccion)
        elif mi_eleccion == "papel" and apuesta_pc == "piedra":
            print("Has perido, la máquina ha sacado", apuesta_pc, "y tu", mi_eleccion)
        elif mi_eleccion == "papel" and apuesta_pc == "tijera":
            print("Has ganado, la máquina ha sacado", apuesta_pc, "y tu", mi_eleccion)
        elif mi_eleccion == "tijera" and apuesta_pc == "papel":
            print("Has perido, la máquina ha sacado", apuesta_pc, "y tu", mi_eleccion)
        elif mi_eleccion == "tijera" and apuesta_pc == "piedra":
            print("Has ganado, la máquina ha sacado", apuesta_pc, "y tu", mi_eleccion)
        else:
            print("Habeis empatado, la máquina ha sacado", apuesta_pc, "y tu", mi_eleccion)
    else:
        print("Solo se puede asignar 'piedra', 'papel' o 'tijera")

#! JUEGO NÚMERO 3
elif selecciona_juego == 3:
    listaPalabras = ['aurora','boreal','lobo','luna','jabali','cabra','queso']
    aciertoFinal = False
    numIntentos = 6
    #opcion 2
    palabraSecreta = getPalabra(listaPalabras)
    estado = transformaPalabra(palabraSecreta)
    #Truco para printar lista sin corchetes

    while aciertoFinal == False and numIntentos > 0:
        print(" ".join(estado))
        #op2
        #print(*estado)
        letra = input('Introduzca una letra: ')
        estado, numIntentos = compruebaLetra(letra, palabraSecreta,estado, numIntentos)

        if compruebaEstado(estado):
            print('Has adivinado la palabra')
            aciertoFinal = True
        else:
            compruebaIntentos(numIntentos)

#! JUEGO NÚMERO 4
elif selecciona_juego == 4:
    print("Juego en mantenimiento")

#! JUEGO NÚMERO 5
elif selecciona_juego == 5:
    print("Juego en mantenimiento")

#! JUEGO NÚMERO 6
elif selecciona_juego == 6:
    print("Juego en mantenimiento")

else:
    print("Error 404: Tienes que elejir un número de juego válido")