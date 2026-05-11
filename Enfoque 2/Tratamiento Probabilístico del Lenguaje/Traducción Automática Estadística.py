from collections import defaultdict

corpus = [
    ("el gato", "the cat"),
    ("el perro", "the dog"),
    ("el gato come", "the cat eats")
]

translation_counts = defaultdict(lambda: defaultdict(int))

for es, en in corpus:
    es_words = es.split()
    en_words = en.split()

    for e in es_words:
        for f in en_words:
            translation_counts[e][f] += 1

def translate(word):
    translations = translation_counts[word]
    if not translations:
        return None
    return max(translations, key=translations.get)

sentence = "el gato"
print([translate(w) for w in sentence.split()])