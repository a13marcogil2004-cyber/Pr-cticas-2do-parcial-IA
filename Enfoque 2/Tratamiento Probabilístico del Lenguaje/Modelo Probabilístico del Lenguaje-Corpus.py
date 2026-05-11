from collections import defaultdict

corpus = "el gato come pescado el gato duerme el perro corre"

words = corpus.split()

bigram = defaultdict(lambda: defaultdict(int))

for i in range(len(words)-1):
    bigram[words[i]][words[i+1]] += 1

def predict(word):
    next_words = bigram[word]
    total = sum(next_words.values())
    probs = {k: v/total for k, v in next_words.items()}
    return probs

print(predict("el"))