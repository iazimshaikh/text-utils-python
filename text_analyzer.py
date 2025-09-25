from collections import Counter
import string

def word_frequency(text):
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    return dict(Counter(words))

def character_frequency(text):
    text = text.replace(" ", "").lower()
    return dict(Counter(text))

def unique_words(text):
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    return set(words)

def most_common_words(text, n=5):
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    return Counter(words).most_common(n)

if __name__ == "__main__":
    text = input("Enter Your text for analysis: ")

    print("\nText Analysis:")
    print("-" * 30)
    print("Word Frequency:", word_frequency(text))
    print("Character Frequency:", character_frequency(text))
    print("Unique Words:", unique_words(text))
    print("Top 5 Most Common Words:", most_common_words(text))
