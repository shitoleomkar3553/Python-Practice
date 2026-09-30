import re
import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer data if required
nltk.download('punkt')
nltk.download('punkt_tab')

# Noisy student feedback
text = """
The lecture was soooo good!!! Sir explained evrything very clearly.
But the notes were nt uploaded on time :( 
The lab was gr8, but PC's were soooo slowwwww...
Plz upload notes ASAP!!! Overall, I loved the class 👍👍
"""

print("Original Feedback:")
print(text)

# Basic word tokenization
tokens = word_tokenize(text)

print("\nTokens:")
print(tokens)

# Simple normalization
normalized_text = text.lower()

# Reduce repeated characters: "soooo" -> "soo", "slowwwww" -> "slow"
normalized_text = re.sub(r'(.)\1{2,}', r'\1\1', normalized_text)

# Expand common abbreviations
abbreviations = {
    "nt": "not",
    "plz": "please",
    "asap": "as soon as possible",
    "gr8": "great",
    "luv": "love"
}

for short, full in abbreviations.items():
    normalized_text = re.sub(r'\b' + short + r'\b', full, normalized_text)

# Tokenize cleaned text
clean_tokens = word_tokenize(normalized_text)

print("\nNormalized Feedback:")
print(normalized_text)

print("\nTokens After Normalization:")
print(clean_tokens)