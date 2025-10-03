
#! TIPOS DE OPERADORES (3 TIPOS)

#! OPERADORES ARTIMÉTICOS
# Esto es una suma
print(3 + 5)

# Esto es una resta
print(3 - 5)

# Esto es una división
print(3 / 5)

# Esto es una multiplicación
print(3 * 5)

# Esto es un operador de módulo (para saber el resto de un número)
print(10 % 3)

# Esto es un división que aproxima el resultado
print(10 // 3)

# Esto es un operador de exponente
print(10 ** 3)

print("Hola " + "Phython " + "Que tal?") 
print("Hola " + str(5)) 

# Esto multiplica hola * 5 que es = hola hola hola hola hola
print("Hola " * 5)

#! OPERADORES COMPARATIVOS

# 3 Mayor que 5
print(3 > 5)

# 3 Menor que 5
print(3 < 5)

# 3 Mayor o igual que 5
print(5 >= 5)

# 3 Menor o igual que 5
print(3 <= 5)

# 3 es igual a 5
print(3 == 5)

# 3 es distinto a 5
print(3 != 5)

# Hola mayor que Phyton
print("Hola" > "Phyton")

# Hola menor que Phyton
print("Hola" < "Phyton")

# Hola mayor o igual que Phyton
print("Hola" >= "Phyton") # Resultado por orden alfabetico por ASCI

# Hola menor o igual que Phyton
print("Hola" >= "Phyton") 

# Hola es igual que Phyton
print("Hola" == "Phyton")

# Hola es distinto que Phyton
print("Hola" != "Phyton")

# Para que cuente por caracteres usar len
print(len("Hola") == len("Hola"))

#! OPERADORES LÓGICOS
# Compara uno y otro, ambos tienen que ser true para ser true
print(3 > 5 and "Hola" > "Phyton")

# Compara uno o otro, con que uno sea verdadero la condición será verdadera
print(3 < 5 or "Hola" > "Phyton")

print(3 < 5 or "Hola" > "Phyton" and 2 == 2)

# Muestra al revés del resultado, osea si es false dirá que es true
print(not (3 > 5))

# false y false = false
# false y true = false
# true y false = false
# true y true = true

#print(3 > 5 not "Hola" > "Phyton")