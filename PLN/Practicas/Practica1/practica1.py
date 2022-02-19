import re
import spacy

archivoEntrada = open('tweets.txt')


for line in archivoEntrada:
	 print(line,end='')

archivoEntrada.close()