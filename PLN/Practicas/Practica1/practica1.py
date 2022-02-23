import re

#lectura del fichero
with open('tweets.txt') as archivoEntrada:
	dataset=archivoEntrada.read()

#comprension de los datos
print(type(dataset))  

#Proceso hashtags
hashtags = re.compile("#\w+") 
resultadoHash = hashtags.findall(dataset)


#print(f"Cantidad de hashtags: {len(resultadoHash)}")

print('Hashtags:', len(resultadoHash))
print("-----------------")
#Proceso arrobas

arrobas = re.compile("@\w+")
resultadoArrobas = arrobas.findall(dataset)

#print(resultadoArrobas)


#print(f"Cantidad arrobas: {len(resultadoArrobas)}")

print('Usuarios:', len(resultadoArrobas))
print("-----------------")

#Proceso horas
horas = re.compile("\d+:\d+\w+")
resultadoHoras = horas.findall(dataset)
valores_unicos = list(dict.fromkeys(resultadoHoras))
tuple(valores_unicos)
#print(resultado)
#print(f"Cantidad horas: {+len(resultadoHoras)}")
#print(valores_unicos)
#print(f"Valores unicos en horas: {len(valores_unicos)}")

print('Horas:', len(resultadoHoras))
print("-----------------")


#Proceso fechas
fechas = re.compile("\d+/\d+/\d+ " and "\d+/\w+/\d+")
resultadoFechas = fechas.findall(dataset)
#print(resultadoFechas)
#print(f"Cantidad de fechas: {len(resultadoFechas)}")

#fechas2= re.compile("\d\d/\d\d")
#resultadoFechas2 = fechas2.findall(dataset)
#print(resultadoFechas2)
#print(len(resultadoFechas2))

print('Fechas:', len(resultadoFechas))
print("-----------------")

#Proceso emotes

emote1 = re.findall("\s:D", dataset)
emote2 = re.findall("\s:p", dataset)
emote3 = re.findall("\s:3",dataset)
emote4 = re.findall("\sXD\s",dataset)
emote5 = re.findall("\s:\(\s",dataset)
emote6 = re.findall("\s:\)\s",dataset)
emote7 = re.findall("\s:\*\s",dataset)


sumaEmotes = len(emote1)+ len(emote2)+len(emote3) + len(emote4)+ len (emote5)+len(emote6)+len(emote7)

print('Emotes', sumaEmotes)
print("-----------------")