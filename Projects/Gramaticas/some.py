import enum
import re
"""res = re.search("c", "abcdef")
print(res)
cadena= "aa||cc|"
patron = re.compile("|")
resultado = patron.search("aa")
print(resultado)

aux=cadena.split("|")

print(aux)"""
lista = [['AA|EB|B'], ['aa|bb|cc']]

for i in lista:
    aux="".join(i)
    aux=aux.split('|')
    for j, elem in enumerate (aux):
        y = aux[j]
        print(y)