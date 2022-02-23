import re
#comprueba si hay una coincidencia en cualquier parte de la cadena
res = re.search("c","abcdef")
print(res)
#permite obtener unalista de todas las cadenas que empatan con un patron
resultado = re.findall("\s", "esta es una cadena")
print(resultado)
#separa una cadena considerando las coincidencias del patron
resultado = re.split("\s","esta es una cadena")
print(resultado)
#busca un patron y lo reemplaza con la cadena establecida
resultado = re.sub("\s","\n", "esta es una cadena")
print(resultado)
#crea un objeto patron el cual puede ser usado en una expresion regular como patron de busqueda
patron = re.compile(",")
resultado = patron.findall("Cadena1,Cadena2,Cadena3,Cadena4,Cadena5")
print(resultado)
resultado2 = patron.split("Cadena1,Cadena2,Cadena3,Cadena4,Cadena5")
print(resultado2)

#ejemplo
patron = re.compile("\d+\:?\d+")
resultado = patron.findall("Esta es una cadena con los numeros 14, 15:5 y 0.25")
print(resultado)

patron = re.compile("\s@\w+")
resultado = patron.findall("Esta es una cadena con los numeros 14, 15:5 y 0.25, leo@leo @H0ra25")
print(resultado)

patron = re.compile("\d+/\d+/\d+ " and "\d+/\w+/\d+")
resultado = patron.findall("Esta es una cadena con los numeros 14, 15:5 y 0.25, leo@leo @H0ra25    04/1/2015  04/enero/2025 7 de enero")
print(resultado)

patron = re.compile(":D?")
resultado = patron.findall("Esta es una cadena con los numeros 14, 15:5 y 0.25, leo@leo @H0ra25  :D  04/1/2015  04/enero/2025 7 de enero")
print(resultado)

