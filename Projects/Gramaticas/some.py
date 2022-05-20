import re
res = re.search("c", "abcdef")
print(res)

patron = re.compile("[a-z]*[A-Z]+[a-z]*")
resultado = patron.search("aa")
print(resultado)