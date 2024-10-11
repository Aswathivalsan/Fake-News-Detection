import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from FakeNewsDetection.fnapp.views import news
from .similarity import levenshtein_similarity
def ongoogle(news):
    n =news
    #n='''A Delhi Court extended Bharat Rashtra Samithi (BRS) leader K Kavitha’s judicial custody till April 23 in the excise policy linked-money laundering case on Tuesday. In a letter to the Rouse Avenue Court, Kavitha called herself a “victim” and said the Enforcement Directorate and Central Bureau of Investigation (CBI) have conducting a “media trial for 2.5 years”.A Delhi Court extended Bharat Rashtra Samithi (BRS) leader K Kavitha’s judicial custody till April 23 in the excise policy linked-money laundering case on Tuesday. In a letter to the Rouse Avenue Court, Kavitha called herself a “victim” and said the Enforcement Directorate and Central Bureau of Investigation (CBI) have conducting a “media trial for 2.5 years”.'''
    res=requests.get("https://www.google.co.in/search?q="+n).text
    res=res.split('<div class="kCrYT">')
    # res=res.split('<div class="BNeawe s3v9rd AP7Wnd">')
    import re
    clean=re.compile('<.*?>')
    news=[]
    for i in range(1,len(res)):
        print(res[i])
    try:
        print(res[i].split('<div class="BNeawe s3v9rd AP7Wnd">'))
        news.append(re.sub(clean," ",res[i].split('<div class="BNeawe s3v9rd AP7Wnd">')[2].split('</div>')[0]))
    except:
        try:
         print(res[i].split('<span class="rQMQod Xb5VRe">')[1].split('</span>'))
        except:
            pass
    # break


    print("===================================================")
    print("===================================================")
    print("===================================================")


    similaritylist = []
    for article in news:
        vectorizer = CountVectorizer().fit([n, article])
        vectorized_text = vectorizer.transform([n, article])


        cosine_sim = cosine_similarity(vectorized_text[0], vectorized_text[1])
        lev_sim = levenshtein_similarity(n, article)

        print("Cosine similarity:", cosine_sim[0][0])
        print("levenshtein_similarity:", lev_sim)
        similaritylist.append(cosine_sim[0][0])
        print(article)
    return similaritylist

    print("===================================================")


