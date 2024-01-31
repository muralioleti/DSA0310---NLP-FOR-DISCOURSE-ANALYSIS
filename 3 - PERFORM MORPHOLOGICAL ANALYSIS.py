import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download necessary resources (uncomment if not already downloaded)
# nltk.download('punkt')
# nltk.download('wordnet')

def morphological_analysis(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Perform stemming using Porter Stemmer
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    
    # Perform lemmatization using WordNet Lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    
    # Print the results
    print(f"Original Text: {text}")
    print(f"Tokenized Words: {words}")
    print(f"Stemmed Words: {stemmed_words}")
    print(f"Lemmatized Words: {lemmatized_words}")

# Example usage
text_to_analyze = "The quick brown foxes are jumping over the lazy dogs"
morphological_analysis(text_to_analyze)
