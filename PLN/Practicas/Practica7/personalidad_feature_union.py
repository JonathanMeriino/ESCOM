import os
import sys
import nltk
import matplotlib.pyplot as plt
from lxml import etree
from features import *
from sklearn import svm
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics import ConfusionMatrixDisplay
def main(argv):
	trainingdir = argv[1]
	testdir = argv[2]
	languages = ['dutch', 'english', 'italian', 'spanish']
        
	for language in languages:
		if language == 'spanish':
			# train the system
			Xtrain, Ytraingender, Ytrainage = [], [], []
			traintweets = loadData(trainingdir, language)
			traintruths = loadTruth(trainingdir, language)
			for author, tweet in traintweets.items():
				Xtrain.extend(tweet)
				##015f2a45-47f5-48bf-904c-264acc3475df:::F:::18-24:::0.1:::0.1:::0.4:::0.2:::0.1
				#truths[split[0]]=(split[1],split[2])
				Ytraingender.extend([traintruths[author][0]] * len(tweet))
				Ytrainage.extend([traintruths[author][1]] * len(tweet))
			
			X_train, X_test, y_train, y_test = train_test_split(Xtrain, Ytrainage, test_size=0.20, random_state=0)
			vectorizer = TfidfVectorizer()
			X_train = vectorizer.fit_transform(X_train)
		
			X_test = vectorizer.transform(X_test)
			
			svd = TruncatedSVD(500)
			X_train = svd.fit_transform(X_train)
			features = FeatureUnion([('tfidf', TfidfVectorizer(analyzer='char', ngram_range=(3,4))),
									 ('patterns', Patterns(['.','!','?','rt','#','@', 'http']))
								
									 ])
			
			#~ features = FeatureUnion([('tfidf', TfidfVectorizer(analyzer='char', ngram_range=(3,4))),
									 #~ ('patterns', Patterns(['.','!','?','rt','#','@', 'http']))
									 #~ ],
									 #~ transformer_weights={'tfidf': 3})
			
			
					
			clf = LogisticRegression(max_iter = 10000,class_weight="balanced",solver="liblinear")
			model = TruncatedSVD()
			pipeline = Pipeline([("Model", model.fit_transform(X_train)),('features', features), ('classifier', clf)])
			pipeline.fit(X_train, y_train)
			
			#Test model
			y_predicted = pipeline.predict(X_test)
			target_names = ['18-24','25-34','35-49','50-XX']
			print(classification_report(y_test, y_predicted, target_names=target_names))
			
			ConfusionMatrixDisplay.from_predictions(y_test, y_predicted)
			plt.show()
			

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

def loadTruth(directory, language):
	#015f2a45-47f5-48bf-904c-264acc3475df:::F:::18-24:::0.1:::0.1:::0.4:::0.2:::0.1
	# returns a dictionary of truth values per author
	truths = {}
	filepath = os.path.join(directory, language, 'truth.txt')
	handle = open(filepath, 'r')
	for line in handle:
		split = line.split(':::')
		truths[split[0]]=(split[1],split[2])
	
	return truths
        

if __name__ == '__main__':
	main(sys.argv)
