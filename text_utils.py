import string

def count_words(text):
    """Count the number of words in the given text."""
    words = text.split()
    return len(words)

def find_longest_word(text):
    """Find the longest word in the given text."""
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

def reverse_text(text):
    """Reverse the given text."""
    return text[::-1]

def capitalize_words(text):
    """Capitalize the first letter of each word in the given text."""
    return ' '.join([word.capitalize() for word in text.split()])

def remove_punctuation(text):
    """Remove all punctuation from the given text."""
    return text.translate(str.maketrans('', '', string.punctuation))

if __name__ == "__main__":
    # Simple menu to test the utility functions
    text = input("Enter some text: ")
    print("\nChoose an option:")
    print("1. Count words")
    print("2. Find the longest word")
    print("3. Reverse text")
    print("4. Capitalize words")
    print("5. Remove punctuation")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print(f"Word count: {count_words(text)}")
    elif choice == "2":
        print(f"Longest word: {find_longest_word(text)}")
    elif choice == "3":
        print(f"Reversed text: {reverse_text(text)}")
    elif choice == "4":
        print(f"Capitalized text: {capitalize_words(text)}")
    elif choice == "5":
        print(f"Text without punctuation: {remove_punctuation(text)}")
    else:
        print("Invalid choice")
