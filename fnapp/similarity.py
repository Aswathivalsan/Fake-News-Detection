from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


text1 = "NLTK is a leading platform for building Python programs to work with human language data."
text2 = "Python is a programming language that lets you work quickly and integrate systems more effectively."


vectorizer = CountVectorizer().fit([text1, text2])
vectorized_text = vectorizer.transform([text1, text2])


cosine_sim = cosine_similarity(vectorized_text[0], vectorized_text[1])




def levenshtein_distance(s1, s2):
    """
    
    """

    distances = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]


    for i in range(len(s1) + 1):
        distances[i][0] = i
    for j in range(len(s2) + 1):
        distances[0][j] = j


    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            distances[i][j] = min(distances[i - 1][j] + 1,       # deletion
                                  distances[i][j - 1] + 1,       # insertion
                                  distances[i - 1][j - 1] + cost)  # substitution

    return distances[len(s1)][len(s2)]



def levenshtein_similarity(sentence1, sentence2):

    distance = levenshtein_distance(sentence1, sentence2)


    max_length = max(len(sentence1), len(sentence2))
    similarity = 1 - distance / max_length

    return similarity


# # Example usage
# sentence1 = "The Malayalis who committed suicide in Arunachal Pradesh were enslaved to bizarre superstitions. The cops who inspected Arya’s laptop were in for a su..."
# sentence2 = "A quick brown dog jumps over the lazy fox"
# similarity = levenshtein_similarity(sentence1, sentence2)
# print("Levenshtein similarity between the sentences is:", similarity)
