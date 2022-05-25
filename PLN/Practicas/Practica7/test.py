import pandas as pd
import xml.etree.ElementTree as ET
import os
from lxml import etree


def loadData(directory, language):
	# returns a dictionary of tweets per author
	tweets = {}
	languagedir = os.path.join(directory, language)
	for filename in os.listdir(languagedir):
		if filename.endswith('xml'):
			handle = open(os.path.join(languagedir, filename), 'rb')
			tree = etree.fromstring(handle.read())
			documents = tree.xpath('//document')
			tweets[filename[:-4]] = [doc.text.rstrip() for doc in documents]
		
	return tweets

loadData('\\/home/jonathan/Documents/Github/ESCOM/PLN/Practicas/Practica7','spanish')