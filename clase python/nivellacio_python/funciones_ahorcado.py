import random

from faker import Faker


def getPalabra(lista):
  palabra = random.choice(lista)
  return palabra

def getPalabraAleatoria():
  fake = Faker('ES-es')
  palabra = fake.word()
  return palabra

def transformaPalabra(palabra):
  estado = []
  for letra in palabra:
    estado.append('_')
  return estado

def reemplazarLetra(palabraSecreta, estado, letra):
  for n in range(0,len(palabraSecreta)):
    if letra == palabraSecreta[n]:
      estado[n] = letra
  return estado

def compruebaEstado(estado):
  if '_' not in estado:
    return True

def compruebaLetra(letra,palabraSecreta,estado,numIntentos):
  if letra in palabraSecreta:
    print('Has elegido una letra correcta')
    estado = reemplazarLetra(palabraSecreta, estado, letra)
  else:
    print('La letra no está en la palabra')
    numIntentos -= 1

  return estado, numIntentos

def compruebaIntentos(numIntentos):
  if numIntentos != 0:
    print(f'Te quedan {numIntentos} intentos')
  else:
    print('Game Over! No te quedan intentos')





