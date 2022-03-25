from gensim.test.utils import common_texts
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from preprocesamiento import *

""""
Modelos para Corpus Tokenizado

"""
tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(datasetToken)] 

#Combinacion dm[0] , vector_size[100] , window[5]
#model01005 = Doc2Vec(tagged_data,dm=0, vector_size=100,window=5)

##Guardar modelo
#model01005.save("doc2vec.modelToken01005") 
## Load saved doc2vec model
model01005= Doc2Vec.load("doc2vec.modelToken01005")
print("Modelo Dataset Tokenizado: dm[0],vector_size[100] , window[5]",model01005.dv.most_similar(model01005.dv[300]),sep='\n')


#Combinacion dm[0] , vector_size[100] , window[10]
#model010010 = Doc2Vec(tagged_data,dm=0, vector_size=100,window=10)

#Guardar modelo
#model010010.save("doc2vec.modelToken010010") 
## Load saved doc2vec model
model010010= Doc2Vec.load("doc2vec.modelToken010010")
print("Modelo Dataset Tokenizado: dm[0],vector_size[100] , window[10]",model010010.dv.most_similar(model010010.dv[87]),sep='\n')


#Combinacion dm[0] , vector_size[300] , window[5]
#model03005 = Doc2Vec(tagged_data,dm=0, vector_size=300,window=5)
#Guardar modelo
#model03005.save("doc2vec.modelToken03005") 
## Load saved doc2vec model
model03005= Doc2Vec.load("doc2vec.modelToken03005")
print("Modelo Dataset Tokenizado: dm[0],vector_size[300] , window[5]",model03005.dv.most_similar(model03005.dv[10]),sep='\n')


#Combinacion dm[0] , vector_size[300] , window[10]
#model030010 = Doc2Vec(tagged_data,dm=0, vector_size=300,window=10)

#Guardar modelo
#model030010.save("doc2vec.modelToken030010") 
## Load saved doc2vec model
model030010= Doc2Vec.load("doc2vec.modelToken030010")
print("Modelo Dataset Tokenizado: dm[0],vector_size[300] , window[10]",model030010.dv.most_similar(model030010.dv[84]),sep='\n')

#Combinacion dm[1] , vector_size[100] , window[5]
#model11005 = Doc2Vec(tagged_data,dm=1, vector_size=100,window=5)

#Guardar modelo
#model11005.save("doc2vec.modelToken11005") 
## Load saved doc2vec model
model11005= Doc2Vec.load("doc2vec.modelToken11005")
print("Modelo Dataset Tokenizado: dm[1],vector_size[100] , window[5]",model11005.dv.most_similar(model11005.dv[34]),sep='\n')

#Combinacion dm[1] , vector_size[100] , window[10]
#model110010 = Doc2Vec(tagged_data,dm=1, vector_size=100,window=10)

#Guardar modelo
#model110010.save("doc2vec.modelToken110010") 
## Load saved doc2vec model
model110010= Doc2Vec.load("doc2vec.modelToken110010")
print("Modelo Dataset Tokenizado: dm[1],vector_size[100] , window[10]",model110010.dv.most_similar(model110010.dv[478]),sep='\n')


#Combinacion dm[1] , vector_size[300] , window[5]
#model13005 = Doc2Vec(tagged_data,dm=1, vector_size=300,window=5)

#Guardar modelo
#model13005.save("doc2vec.modelToken13005") 
## Load saved doc2vec model
model13005= Doc2Vec.load("doc2vec.modelToken13005")
print("Modelo Dataset Tokenizado: dm[1],vector_size[300] , window[5]",model13005.dv.most_similar(model13005.dv[212]),sep='\n')



#Combinacion dm[1] , vector_size[300] , window[10]
#model130010 = Doc2Vec(tagged_data,dm=1, vector_size=300,window=10)

#Guardar modelo
#model130010.save("doc2vec.modelToken130010") 
## Load saved doc2vec model
model130010= Doc2Vec.load("doc2vec.modelToken130010")
print("Modelo Dataset Tokenizado: dm[1],vector_size[300] , window[10]",model130010.dv.most_similar(model130010.dv[105]),sep='\n')


""""
Modelos para Corpus Practica 2

"""
#tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(nuevoDataset)]  # asignar etiquetas
#print(tagged_data[0:2])

#Combinacion dm[0] , vector_size[100] , window[5]
#model01005 = Doc2Vec(tagged_data,dm=0, vector_size=100,window=5)

#Guardar modelo
#model01005.save("doc2vec.model01005") 
## Load saved doc2vec model
#model01005= Doc2Vec.load("doc2vec.model01005")
#print("Modelo Dataset dm[0],vector_size[100] , window[5]",model01005.dv.most_similar(model01005.dv[0]),sep='\n')



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