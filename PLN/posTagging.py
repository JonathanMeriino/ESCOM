#Importamos la biblioteca spacy
import spacy
from spacy import displacy

#~ cadena = "Juan estaba corriendo velozmente por el pasillo. "
cadena = "Los perros ladraron la otra noche a unos coches rojos que pasaron por la calle."

#Se carga el corpus para el tagger en español
nlp = spacy.load("es_core_news_sm")
#Se realiza el análisis de la cadena
doc = nlp(cadena)

for token in doc:
    #~ print(token.text, token.pos_, token.dep_)
    print(token.text, token.pos_, token.dep_, token.lemma_)
#~ displacy.serve(doc, style="dep")    
