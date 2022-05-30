import os
import sys
import nltk
import matplotlib.pyplot as plt
from lxml import etree
from features import *
from sklearn import svm
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, HashingVectorizer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from nltk.corpus import stopwords
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.decomposition import TruncatedSVD
from sklearn import linear_model
# nltk.download('stopwords')
# stopwords = [word.decode('utf-8') for word in stopwords.words('spanish')]


def main(argv):
	trainingdir = argv[2]
	testdir = argv[1]
	languages = ['dutch', 'english', 'italian', 'spanish']
        
	for language in languages:
		if language == 'spanish':
			# train the system
			Xtrain, Ytraingender, Ytrainage = [], [], []
			traintweets = loadData(trainingdir, language)
			traintruths = loadTruth(trainingdir, language)

# 			X_train = traintweets.data
# 			y_train = traintweets.target
# 			X_test = traintruths.data
# 			y_test = traintruths.target

# 			#~ print (newsgroups_train.target.shape)
# 			#~ print (newsgroups_train.target[:10])

# 			vectorizer = TfidfVectorizer()
# 			vectors_train = vectorizer.fit_transform(traintweets.data)

# 			clf = LogisticRegression()
# 			clf.fit(vectors_train, y_train)

# 			vectors_test = vectorizer.transform(traintruths.data)
# 			y_pred = clf.predict(vectors_test)
# 			#~ print (y_pred)
# 			print ('vectors_train.shape {}'.format(vectors_train.shape))
# 			print ('vectors_test.shape {}'.format(vectors_test.shape))



# 			print (classification_report(y_test, y_pred))
            
            
			for author, tweet in traintweets.items():
				Xtrain.extend(tweet)
				##015f2a45-47f5-48bf-904c-264acc3475df:::F:::18-24:::0.1:::0.1:::0.4:::0.2:::0.1
				#truths[split[0]]=(split[1],split[2])
				Ytraingender.extend([traintruths[author][0]] * len(tweet))
				Ytrainage.extend([traintruths[author][1]] * len(tweet))
			
			X_train, X_test, y_train, y_test = train_test_split(Xtrain, Ytrainage, test_size=0.2, random_state=0)
			
# 			vectorizer = TfidfVectorizer()
# 			vectors_train = vectorizer.fit_transform(X_train)

# 			clf = LogisticRegression()
# 			clf.fit(vectors_train, y_train)

# 			vectors_test = vectorizer.transform(X_test)
# 			y_pred = clf.predict(vectors_test)
# 			#~ print (y_pred)
# 			print ('vectors_train.shape {}'.format(vectors_train.shape))
# 			print ('vectors_test.shape {}'.format(vectors_test.shape))



# 			print (classification_report(y_test, y_pred))            


			#Modelo con Hashing
#			features = FeatureUnion([('Hashing', HashingVectorizer(binary=True, analyzer='word', stop_words=stopwords.words("spanish") , ngram_range=(3,4))),
# 									 ('patterns', Patterns(['.','!','?','rt','#','@', 'http']))
# 									 ])
            
            
			#Modelo con tfidf Binariotokenizercallable, default=None
# 			features = FeatureUnion([('tfidf', TfidfVectorizer(binary=True,analyzer='char', ngram_range=(3,4))),
#  									 ('patterns', Patterns(['.','!','?','rt','#','@', 'http']))
#  									 ])

			#Modelo con tfidf
			# ~ features = FeatureUnion([('tfidf', TfidfVectorizer(binary=True,analyzer='char_wb',strip_accents='unicode',ngram_range=(3,4))),
									 # ~ ('patterns', Patterns(['.','!','?','rt','#','@', 'http']))
									 # ~ ])

			#Modelo con frecuencia Vectorial
# 			features = FeatureUnion([('Frecuencia', CountVectorizer(analyzer='char', ngram_range=(3,4))),
# 									 ('patterns', Patterns(['.','!','?','rt','#','@', 'http']))
# 									 ])

            #Modelo Vectorizador Binario
#			features = FeatureUnion([('Binario', CountVectorizer(binary=True,analyzer='char', ngram_range=(3,4))),
#									 ('patterns', Patterns(['.','!','?','rt','#','@', 'http']))
#									 ])            
			
			features = FeatureUnion([('tfidf', TfidfVectorizer( analyzer='char_wb', ngram_range=(1,6),strip_accents='unicode')),
									 ('patterns', Patterns([':)',':S',':P',':D',':O',':(', 'u.u'])),
									 ],
									 transformer_weights={'tfidf': 4})
			
			#Train model
			clf = LogisticRegression(max_iter = 10000,class_weight="balanced",solver="liblinear")
			#clf = TruncatedSVD()
			pipeline = Pipeline([('features', features),
                        ('classifier', clf)])
			pipeline.fit(X_train, y_train)
			
			#Test model
			y_predicted = pipeline.predict(X_test)
			target_names = ['18-24','25-34','35-49','50-XX']
			print(classification_report(y_test, y_predicted, target_names=target_names))
			
			ConfusionMatrixDisplay.from_predictions(y_test, y_predicted)
			plt.show()
			"""#Model LSA
			vectorizer = TfidfVectorizer()
			vectors_train = vectorizer.fit_transform(X_train)
		
			vectors_test = vectorizer.transform(X_test)
			
			svd = TruncatedSVD(500)
			vectors_train_lsa = svd.fit_transform(vectors_train)
			clf.fit(vectors_train_lsa, y_train)

			vectors_test_lsa = svd.transform(vectors_test)

			y_pred = clf.predict(vectors_test_lsa)
			print (classification_report(y_test, y_pred))"""

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
