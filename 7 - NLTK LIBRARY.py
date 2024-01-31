import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download the NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):
    # Tokenize the input text into words
    words = word_tokenize(text)
    
    # Perform part-of-speech tagging
    tagged_words = pos_tag(words)
    
    return tagged_words

# Example usage
text = "NLTK is a powerful library for natural language processing in Python."
tagged_text = pos_tagging(text)

print("Original text:")
print(text)
print("\nPart-of-speech tagged text:")
print(tagged_text)
