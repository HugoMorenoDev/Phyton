
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

#! JUEGO NÚMERO 1 ADIVINA NUMERO
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

#! JUEGO NÚMERO 2 PIEDRA PAPEL TIJERA
elif selecciona_juego == 2:
    import random
    print("Tienes que sacar piedra, papel o tijera y juegas contra la máquina")

    def obtener_eleccion_usuario():
        eleccion = input("Elije entre 'piedra', 'papel' o 'tijera'" \
        "\n¿Qué elijes?: ")
        return eleccion.lower().strip()

    def mostrar_resultado(mi_eleccion, apuesta_pc, resultado):
        print(f"{resultado}, la máquina ha sacado {apuesta_pc} y tú {mi_eleccion}")

    posibilades = ["piedra", "papel", "tijera"]
    apuesta_pc = random.choice(posibilades)
    mi_eleccion = obtener_eleccion_usuario()

    if mi_eleccion == "tijera" or mi_eleccion == "papel" or mi_eleccion == "piedra":
        if mi_eleccion == "piedra" and apuesta_pc == "papel":
            mostrar_resultado(mi_eleccion, apuesta_pc, "Has perdido")
        elif mi_eleccion == "piedra" and apuesta_pc == "tijera":
            mostrar_resultado(mi_eleccion, apuesta_pc, "Has ganado")
        elif mi_eleccion == "papel" and apuesta_pc == "piedra":
            mostrar_resultado(mi_eleccion, apuesta_pc, "Has ganado")
        elif mi_eleccion == "papel" and apuesta_pc == "tijera":
            mostrar_resultado(mi_eleccion, apuesta_pc, "Has perdido")
        elif mi_eleccion == "tijera" and apuesta_pc == "papel":
            mostrar_resultado(mi_eleccion, apuesta_pc, "Has ganado")
        elif mi_eleccion == "tijera" and apuesta_pc == "piedra":
            mostrar_resultado(mi_eleccion, apuesta_pc, "Has perdido")
        else:
            mostrar_resultado(mi_eleccion, apuesta_pc, "Habéis empatado")
    else:
        print("Solo se puede asignar 'piedra', 'papel' o 'tijera'")

#! JUEGO NÚMERO 3 AHORCADO
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

#! JUEGO NÚMERO 4 TRES EN RAYA
elif selecciona_juego == 4:
    print("Juego en mantenimiento")

#! JUEGO NÚMERO 5 BLACKJACK
elif selecciona_juego == 5:
    import random

    lista_palos_blackjack = ["Oros", "Copas", "Espadas", "Bastos"]
    lista_valores_blackjack = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    baraja_blackjack = [[valor, palo] for valor in lista_valores_blackjack for palo in lista_palos_blackjack]

    jugar = True

    def jugar_blackjack():
        puntuacion_total = 0
        while True:
            sacar_carta = input(f"Cartas actuales: {len(baraja_blackjack)}. ¿Sacamos carta? (si/no) ").lower()
            if sacar_carta == "si":
                carta_blackjack = random.sample(baraja_blackjack, 1)[0]
                print(f"Valor sacado: {carta_blackjack}")
                baraja_blackjack.remove(carta_blackjack)
                puntuacion_total += carta_blackjack[0]
                print(f"Puntuación total: {puntuacion_total}")
                if puntuacion_total > 21:
                    print("Has obtenido más de 21 puntos, has perdido!")
                    break
            elif sacar_carta == "no":
                break
            else:
                print("¿Puedes repetir por favor?")
        return puntuacion_total

    # --- Jugador 1 ---
    while True:
        jugador1 = input("¿Quieres jugar al blackjack? (si/no): ").lower()
        if jugador1 == "si":
            total_puntos = jugar_blackjack()
            break
        elif jugador1 == "no":
            print("Tú te lo pierdes!")
            exit()
        else:
            print("¿Cómo? No te he entendido")

    total_puntos_jugador1 = total_puntos

    if total_puntos_jugador1 <= 21:
        print("Muy bien, veamos cómo lo hace el segundo jugador...")

    # --- Jugador 2 ---
    while True:
        jugador2 = input("¿Quieres jugar al blackjack? (si/no): ").lower()
        if jugador2 == "si":
            total_puntos = jugar_blackjack()
            break
        else:
            print("¡Ya has quedado con tu amigo para jugar... JUEGA!")

    total_puntos_jugador2 = total_puntos

    if total_puntos_jugador2 <= 21:
        print("Muy bien, es hora de desvelar las cartas de los dos!")

    print(f"Total puntos jugador 1: {total_puntos_jugador1}")
    print(f"Total puntos jugador 2: {total_puntos_jugador2}")

    if total_puntos_jugador1 == total_puntos_jugador2:
        print("¡Habéis empatado!")
    elif total_puntos_jugador1 > total_puntos_jugador2:
        print("¡Jugador 1 ha ganado!")
    else:
        print("¡Jugador 2 ha ganado!")

#! JUEGO NÚMERO 6
elif selecciona_juego == 6:
    print("Juego en mantenimiento")

else:
    print("Error 404: Tienes que elejir un número de juego válido")