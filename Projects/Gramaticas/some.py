import re
res = re.search("c", "abcdef")
print(res)
cadena= "aa||cc|"
patron = re.compile("|")
resultado = patron.search("aa")
print(resultado)

aux=cadena.split("|")

print(aux)
