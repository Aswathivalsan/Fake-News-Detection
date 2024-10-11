txt=input("Enter news : ")

import csv
n=[]
y=[]

fake=[]
real=[]


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

tokens = word_tokenize(txt.lower())

stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]


print(filtered_tokens)




