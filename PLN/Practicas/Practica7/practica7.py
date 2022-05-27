import os
import pandas as pd
from lxml import etree
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from features import *
from sklearn.decomposition import TruncatedSVD
#Pre-procesamiento del corpus
tweets = {}
for filename in os.listdir('train'):
    if filename.endswith('xml'):
        handle = open(os.path.join('train', filename), 'rb')
        tree = etree.fromstring(handle.read())
        documents = tree.xpath('//document')

        tweets[filename[:-4]] = [doc.text.rstrip() for doc in documents]



#Conversion a un dataframe
df = pd.DataFrame([[key, tweets[key]] for key in tweets.keys()], columns=['User', 'Tweets'])
print(df)

tw = df['Tweets']


df['TweetString'] = df['Tweets'].apply(lambda x: ','.join(map(str, x)))
print(df.iloc[:,1:3])

x = df['TweetString'].values

y = df['User'].values

#Split de datos en 80% training y 20% prueba
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=.20, shuffle=True, random_state=0)


"""
features= FeatureUnion([('tfidf', TfidfVectorizer(analyzer='char', ngram_range=(3,4))),
                        ('patterns', Patterns(['.','!','?','rt','#','@', 'http']))
                        ])"""

features= FeatureUnion([('tfidf', TfidfVectorizer( ngram_range=(3,4))),
                       ("svd", TruncatedSVD(n_components=2))])


#Train model
clf=LogisticRegression(max_iter = 10000)
pipeline= Pipeline([('features', features), ('classifier', clf)])
pipeline.fit(x_train, y_train)

#test model
y_pred = pipeline.predict(x_test)
target_names = ['18-24','25-34','35-49','50-XX']
print(classification_report(y_test, y_pred))