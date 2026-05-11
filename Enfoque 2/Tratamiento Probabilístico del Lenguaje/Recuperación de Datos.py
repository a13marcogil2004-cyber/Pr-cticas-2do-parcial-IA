from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs = [
    "las redes neuronales son modelos de IA",
    "los gatos son animales domésticos",
    "el aprendizaje profundo usa redes neuronales"
]

query = ["redes neuronales"]

vectorizer = TfidfVectorizer()

tfidf = vectorizer.fit_transform(docs + query)

similarities = cosine_similarity(tfidf[-1], tfidf[:-1])

print(similarities)