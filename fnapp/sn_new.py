
from bs4 import BeautifulSoup
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fnapp.similarity import levenshtein_similarity
import feedparser
import re
pattern = re.compile('<.*?>')

def fetch_news_articles(qry):
    qry=qry.replace(' ',"+")
    rss_url = 'https://news.google.com/rss/search?q='+qry+'&hl=en-IN&gl=IN&ceid=IN:en'
    feed = feedparser.parse(rss_url)
    similaritylist = []
    if feed.status == 200:
        for entry in feed.entries:
            title = re.sub(pattern, '', entry.title)
            description = re.sub(pattern, '', entry.description)


            print("Title:", title)
            print("Description:", description)
            vectorizer = CountVectorizer().fit([qry, title+" "+description])
            vectorized_text = vectorizer.transform([qry,  title+" "+description])

            # Calculate cosine similarity between the two vectors
            cosine_sim = cosine_similarity(vectorized_text[0], vectorized_text[1])
            lev_sim = levenshtein_similarity(qry,  title+" "+description)

            print("Cosine similarity:", cosine_sim[0][0])
            print("levenshtein_similarity:", lev_sim)
            similaritylist.append(cosine_sim[0][0])

    return similaritylist





# print(fetch_news_articles("bomb blast in kannur"))