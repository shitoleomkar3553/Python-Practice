import spacy

nlp = spacy.load("en_core_web_sm")

text = open("dataset.txt").read()

doc = nlp(text)

print("SYNTACTIC ANALYSIS")
print("=" * 50)

for sentence in doc.sents:

    print("\nSentence:", sentence.text)
    print("-" * 50)

    print("Dependency Parsing:")

    for token in sentence:
        print(token.text, "->", token.dep_, "->", token.head.text)