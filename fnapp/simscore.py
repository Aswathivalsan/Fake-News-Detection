import csv
n=[]
y=[]

fake=[]
real=[]

from sklearn.feature_extraction.text import CountVectorizer


from fnapp.similarity import levenshtein_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer




c=0
with open('Fake.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  try:
      for lines in csvFile:
          print(lines)

          tokens = word_tokenize(lines[0])


          stop_words = set(stopwords.words('english'))
          filtered_tokens = [token for token in tokens if token.lower() not in stop_words]


          stemmer = PorterStemmer()
          stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
          n.append(' '.join(stemmed_tokens))
          fake.append(' '.join(stemmed_tokens))
          y.append(0)
          c=c+1
          if c>=1000:
              break
  except:
      print(0)
      pass

c=0
with open('True.csv', mode ='r', encoding='utf-8')as file:
  csvFile = csv.reader(file)
  try:
      for lines in csvFile:
          print(lines)

          tokens = word_tokenize(lines[0])

          stop_words = set(stopwords.words('english'))
          filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

          stemmer = PorterStemmer()
          stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
          n.append(' '.join(stemmed_tokens))
          real.append(' '.join(stemmed_tokens))
          y.append(1)
          c = c + 1
          if c >= 1000:
              break
  except Exception as e:
      s=e
      print(e)
      print(1)
      pass

def simcheck(txt):
    fs=0
    for i in fake:

        cosine_sim = levenshtein_similarity(i, txt)
        if cosine_sim>fs:
            fs=cosine_sim
    rs = 0
    for i in real:
        cosine_sim = levenshtein_similarity(i, txt)
        if cosine_sim > rs:
            rs = cosine_sim
    return fs,rs

#print(simcheck("Vallyayi (Kannur): The accused in the murder of Vishnupriya (25) was found guilty of breaking into her house, slitting her throat and cutting her veins in Vallyayi near Panoor out of enmity as she had withdrawn from their relationship.M Shyamjith (28) of Thazhekalathil House at Manantheri is the convict. The sentence will be announced on Monday."))