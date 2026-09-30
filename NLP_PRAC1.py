import spacy

nlp = spacy.load("en_core_web_sm")

text = open("dataset.txt").read()

doc = nlp(text)

print("NAMED ENTITY RECOGNITION")
print("=" * 50)

for ent in doc.ents:
    print(ent.text, "->", ent.label_)