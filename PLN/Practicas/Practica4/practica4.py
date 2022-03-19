from gensim.test.utils import common_texts
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import re


#lectura del corpus lematizados
with open ('corpusFinal.txt') as corpusEntrada:
	dataset = corpusEntrada.read()

dataset = re.split('\n',dataset) # conversion del dataset en una lista

#print(dataset[0])

nuevoDataset=[]
for i in dataset:
    aux = re.split("\s", i)

    nuevoDataset.append(aux)

#print(nuevoDataset[0])

tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(nuevoDataset)]  # asignar etiquetas

#print(tagged_data[0:2])

""""
Modelos

"""

#Combinacion dm[0] , vector_size[100] , window[5]
model01005 = Doc2Vec(tagged_data,dm=0, vector_size=100,window=5)

#Guardar modelo
model01005.save("doc2vec.model01005") 
## Load saved doc2vec model
model01005= Doc2Vec.load("doc2vec.model01005")
print(model01005.dv.most_similar(model01005.dv[129]))



#Combinacion dm[0] , vector_size[100] , window[10]
#model010010 = Doc2Vec(tagged_data,dm=0, vector_size=100,window=10)
"""
#Guardar modelo
model010010.save("doc2vec.model010010") 
## Load saved doc2vec model
model010010= Doc2Vec.load("doc2vec.model010010")

"""

#Combinacion dm[0] , vector_size[300] , window[5]
#model03005 = Doc2Vec(tagged_data,dm=0, vector_size=300,window=5)
"""
#Guardar modelo
model03005.save("doc2vec.model03005") 
## Load saved doc2vec model
model03005= Doc2Vec.load("doc2vec.model03005")

"""

#Combinacion dm[0] , vector_size[300] , window[10]
#model030010 = Doc2Vec(tagged_data,dm=0, vector_size=300,window=10)
"""
#Guardar modelo
model030010.save("doc2vec.model030010") 
## Load saved doc2vec model
model030010= Doc2Vec.load("doc2vec.model030010")

"""

#Combinacion dm[1] , vector_size[100] , window[5]
#model11005 = Doc2Vec(tagged_data,dm=1, vector_size=100,window=5)
"""
#Guardar modelo
model11005.save("doc2vec.model11005") 
## Load saved doc2vec model
model11005= Doc2Vec.load("doc2vec.model11005")

print(model.dv.most_similar(model.dv[3]))
"""

#Combinacion dm[1] , vector_size[100] , window[10]
#model110010 = Doc2Vec(tagged_data,dm=1, vector_size=100,window=10)
"""
#Guardar modelo
model110010.save("doc2vec.model110010") 
## Load saved doc2vec model
model110010= Doc2Vec.load("doc2vec.model110010")

"""

#Combinacion dm[1] , vector_size[300] , window[5]
#model13005 = Doc2Vec(tagged_data,dm=1, vector_size=300,window=5)
"""
#Guardar modelo
model13005.save("doc2vec.model13005") 
## Load saved doc2vec model
model13005= Doc2Vec.load("doc2vec.model13005")

"""


#Combinacion dm[1] , vector_size[300] , window[10]
#model130010 = Doc2Vec(tagged_data,dm=1, vector_size=300,window=10)
"""
#Guardar modelo
model130010.save("doc2vec.model130010") 
## Load saved doc2vec model
model130010= Doc2Vec.load("doc2vec.model130010")

"""