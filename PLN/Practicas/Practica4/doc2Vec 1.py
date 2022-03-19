from gensim.models.doc2vec import Doc2Vec, TaggedDocument
#https://radimrehurek.com/gensim/models/doc2vec.html

sentences = [['i', 'like', 'apple', 'pie', 'for', 'dessert'],
           ['i', 'dont', 'drive', 'fast', 'cars'],
           ['data', 'science', 'is', 'fun'],
           ['chocolate', 'is', 'my', 'favorite'],
           ['my', 'favorite', 'movie', 'is', 'predator'],
           ['vanilla', 'is', 'my', 'favorite'],
           ['chocolate', 'is', 'delicious'],
           ['vanilla', 'is', 'delicious']]

tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(sentences)]  # asignar etiquetas

print(tagged_data)

## Train doc2vec model
model = Doc2Vec(tagged_data, vector_size=30)
print(model.dv[0])
print(len(model.dv))
# Save trained doc2vec model
model.save("test_doc2vec.model")
## Load saved doc2vec model
model= Doc2Vec.load("test_doc2vec.model")
## Print model vocabulary
print(model.wv.key_to_index)

print(model.dv.most_similar(model.dv[3]))

