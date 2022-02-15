#Se crean las colecciones (lenguajes) vacios
lenguage=set()
lenguage2=set()

##Se define el tamaño de los lenguajes y se procede a llenarlos mediante datos introducidos por el usuario
#Primer lenguaje
lengthLenguage=int(input("Ingresa la longitud del primer lenguaje: "))
for f in range(0,lengthLenguage):
    aux=input("ingresa una cadena: ")
    lenguage.add(aux)

#Segundo lenguaje
lengthLenguage2=int(input("Ingresa la longitud del segundo lenguaje: "))
for f in range(0,lengthLenguage2):
    aux=input("ingresa una cadena: ")
    lenguage2.add(aux)

#Impresión de las cadenas de ambos lenguajes
print("El primer lenguaje es: ",lenguage)
print("El segundo lenguaje es: ", lenguage2)

##Operaciones de lenguajes
#Unión, intersección y diferencia
#union=lenguage|lenguage2
#intersection=lenguage & lenguage2
#difference=lenguage-lenguage2
print("La unión es: ", lenguage|lenguage2)
print("La intersección es: ", lenguage & lenguage2)
print("La diferencia tipo 'A - B' es: ", lenguage-lenguage2)
#difference=lenguage2-lenguage
print("La diferencia tipo 'B - A' es: ", lenguage2-lenguage)

#Subconjuntos
if lenguage<= lenguage2:
    print("el primer lenguaje es un sublenguaje del segundo")
elif lenguage2<=lenguage:
    print("El segundo lenguaje es un sublenguaje del primero")
else:
    print("No son sublenguajes")    
