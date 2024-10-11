
from bs4 import BeautifulSoup
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fnapp.similarity import levenshtein_similarity
def Yahoo(txt):
    headers = {
        'User-agent':
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }

    def get_organic_results(n):
        # n = "kannur: One person was killed and another seriously injured in a blast near Panur in this north Kerala district in the early hours of Friday, police said. The incident took place at 1 am on Friday. Sherin, a resident of Kaivelikkal, passed away while receiving treatment at a private hospital in Kozhikode. "
        html = requests.get('https://search.yahoo.com/search?p='+n, headers=headers).text
        soup = BeautifulSoup(html, 'html')

        results = []

        for result in soup.find_all('div', class_='compText aAbs'):
            title = result.find('span', class_='fc-falcon').text
            results.append(title)

        return results

    n = txt
    # n = "kannur: One person was killed and another seriously injured in a blast near Panur in this north Kerala district in the early hours of Friday, police said. The incident took place at 1 am on Friday. Sherin, a resident of Kaivelikkal, passed away while receiving treatment at a private hospital in Kozhikode. "


    news = get_organic_results(n)


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
