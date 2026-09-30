import nltk

text = open("dataset.txt").read()

sentences = nltk.sent_tokenize(text)

print("MORPHOLOGICAL ANALYSIS AND POS TAGGING")
print("=" * 50)

for sentence in sentences:
    print("\nSentence:", sentence)
    print("-" * 50)

    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)

    for word, tag in tags:
        if word.isalpha():
            print(word, "->", tag)