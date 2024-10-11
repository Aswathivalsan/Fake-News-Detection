

from bs4 import BeautifulSoup
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fnapp.similarity import levenshtein_similarity
headers = {
        'User-agent':
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

def onmanorama(query):

    html = requests.get("https://www.onmanorama.com/search-results.html?q=" + query , headers=headers).text
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    results = []

    for result in soup.find_all('div', class_='storylist-content'):
        title = result.find(class_='listing-title-002')
        snippet = result.find(class_='listing-dispn-p')
        if title and snippet:
            results.append((title.text+" "+snippet.text,title.text+" "+snippet.text))


    n = query


    similaritylist = []
    for article in results:

        vectorizer = CountVectorizer().fit([n, article[0]])
        vectorized_text = vectorizer.transform([n, article[0]])


        cosine_sim = cosine_similarity(vectorized_text[0], vectorized_text[1])
        lev_sim = levenshtein_similarity(n, article)

        print("Cosine similarity:", cosine_sim[0][0])
        print("levenshtein_similarity:", lev_sim)
        similaritylist.append(cosine_sim[0][0])
        print(article)
    return similaritylist

