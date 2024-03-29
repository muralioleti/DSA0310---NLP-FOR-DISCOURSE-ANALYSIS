import nltk
from nltk.stem import PorterStemmer

# Download necessary resources (uncomment if not already downloaded)
# nltk.download('punkt')

def porter_stemming(words):
    # Initialize the Porter Stemmer
    stemmer = PorterStemmer()
    
    # Perform stemming on each word in the list
    stemmed_words = [stemmer.stem(word) for word in words]
    
    return stemmed_words

# Example usage
word_list = ["running", "easily", "jumps", "happily", "better"]
stemmed_words = porter_stemming(word_list)

# Print the results
print("Original Words:", word_list)
print("Stemmed Words:", stemmed_words)
