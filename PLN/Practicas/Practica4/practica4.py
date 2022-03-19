from gensim.test.utils import common_texts
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import re


#lectura del corpus lematizados
with open ('corpusFinal.txt') as corpusEntrada:
	dataset = corpusEntrada.read()

dataset = re.split('\n',dataset) # conversion del dataset en una lista

print(dataset[0])

nuevoDataset=[]
for i in dataset:
    aux = re.split("\s", i)

    nuevoDataset.append(aux)

print(nuevoDataset[0])

tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(nuevoDataset)]  # asignar etiquetas

print(tagged_data[0:2])

""""
Modelos

"""

#Combinacion dm[0] , vector_size[100] , window[5]
model = Doc2Vec(tagged_data, vector_size=30)
#Combinacion dm[0] , vector_size[100] , window[10]

#Combinacion dm[0] , vector_size[300] , window[5]

#Combinacion dm[0] , vector_size[300] , window[10]

#Combinacion dm[1] , vector_size[100] , window[5]

#Combinacion dm[1] , vector_size[100] , window[10]


#Combinacion dm[1] , vector_size[300] , window[5]


#Combinacion dm[1] , vector_size[300] , window[10]
