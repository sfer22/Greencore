# Tema Hileras

message = input("Digite lo que quiera: ")

print(message)

#len() -> Encontrar la cantidad de caracteres que tiene una hilera

print(len(message))

# Indices

print(message[0]) #Obtenemos el primer caracter de una hilera
print(message[len(message) - 1]) #Obtenemos el ultimo caracter de una hilera

#Concatenacion de hileras

hilera = "Hilera inicial"

#Concatenacion simple

print(hilera + " otra hilera")
print(hilera)

#Concatenacion modificando la variable

hilera += ". Esto si modifica la variable hilera"
print(hilera)

#Inyectando texto
# {} Wilcard. para poner texto dinamicamente.

otra_hilera = "Hola {}! como esta?".format("Steve") #se le puede pasar mas de un {} a format.
print(otra_hilera)
print(otra_hilera[3:10]) #imprimir entre las posiciones 3 y 10 del string
print(otra_hilera[:10]) #imprimir las primeras 10 posiciones
print(otra_hilera[10:]) #imprimir desde la posicion 10
print(otra_hilera[::-1])



