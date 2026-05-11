import spacy

nlp = spacy.load("es_core_news_sm")

text = "María compró un teléfono en Guadalajara el 10 de mayo"

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)