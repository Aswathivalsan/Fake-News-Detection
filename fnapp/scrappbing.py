from bs4 import BeautifulSoup
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fnapp.similarity import levenshtein_similarity

def Onbing(txt):
    headers = {
    'User-agent':
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }
    def get_organic_results(query):

        print("https://www.bing.com/search?q=" + query)
        html = requests.get("https://www.bing.com/search?q=" + query, headers=headers).text
        # html = requests.get("https://www.bing.com/search?q=" + query).text
        soup = BeautifulSoup(html, 'html.parser')
        results = []
        # print(html)

        for result in soup.find_all('li', class_='b_algo'):
          title = result.find('a')
          snippet = result.find('div', class_='b_caption').find('p')
          if title and snippet:
               results.append((title.text, snippet.text))

        return results


    n=txt
    # n = "A Delhi Court extended Bharat Rashtra Samithi (BRS) leader K Kavitha’s judicial custody till April 23 in the excise policy linked-money laundering case on Tuesday. In a letter to the Rouse Avenue Court, Kavitha called herself a “victim” and said the Enforcement Directorate and Central Bureau of Investigation (CBI) have conducting a “media trial for 2.5 years”."

    # Get organic search results
    news = get_organic_results(n)
    print(news)

    similaritylist = []
    for article in news:
        print("======================================================")
        print(article)
        try:
            vectorizer = CountVectorizer().fit([n, article[1]])
            vectorized_text = vectorizer.transform([n, article[1]])


            cosine_sim = cosine_similarity(vectorized_text[0], vectorized_text[1])
            lev_sim = levenshtein_similarity(n, article[1])

            print("Cosine similarity:", cosine_sim[0][0])
            print("levenshtein_similarity:", lev_sim)
            similaritylist.append(cosine_sim[0][0])
            print(article)
        except:
            pass
    return similaritylist
#print(Onbing('''The body of a newborn was found on the road next to an apartment in Vidyanagar, Kochi on Friday. It is suspected that the baby was thrown from a vacant apartment.Authorities have taken three people into custody in relation to the case. Among them are two women and a man. Details were not revealed but investigators have found bloodstains in the flat's restroom, suggesting it may be linked to the birth of a baby. Further information on this case is expected'''))