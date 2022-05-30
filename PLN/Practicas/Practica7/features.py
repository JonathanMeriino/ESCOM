from collections import defaultdict
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
class Capitals(BaseEstimator, TransformerMixin):
        # feature that counts capitalized characters in a tweet
        def fit(self, X, Y=None):
                return self
        def transform(self, X):
                return [[sum(1 for ch in doc if ch.isupper())] for doc in X]

class Patterns(BaseEstimator, TransformerMixin):
        # feature that counts occurences for a range of patterns
        def __init__(self, patterns):
                self.patterns = patterns
        def fit(self, X, Y=None):
                return self
        def transform(self, X):
                return [[doc.lower().count(pattern)/len(doc) for pattern in self.patterns] for doc in X]

class LSA:
        def __init__ (self, X_train):
                self.X_train = X_train
        def convert(self, X_train):
            vectorizer = TfidfVectorizer()
            vectors_train = vectorizer.fit_transform(X_train)
            
            return vectors_train
                            