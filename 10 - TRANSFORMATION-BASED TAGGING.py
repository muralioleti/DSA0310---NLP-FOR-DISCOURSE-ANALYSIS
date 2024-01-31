import nltk

# Sample training data
training_data = [
    ('The', 'DET'), ('quick', 'ADJ'), ('brown', 'ADJ'), ('cat', 'NOUN'),
    ('is', 'VERB'), ('on', 'PREP'), ('the', 'DET'), ('mat', 'NOUN')
]

# Transformation rule: If a word is preceded by 'the' and followed by 'NOUN', tag it as 'ADJ'
def apply_transformation_rules(tagged_sentence):
    for i in range(1, len(tagged_sentence) - 1):
        if tagged_sentence[i-1][0].lower() == 'the' and tagged_sentence[i+1][1] == 'NOUN':
            tagged_sentence[i] = (tagged_sentence[i][0], 'ADJ')
    return tagged_sentence

# Apply transformation rules to the training data
tagged_data = apply_transformation_rules(training_data)

# Example usage
test_sentence = "The quick brown cat is on the mat"
test_tokens = nltk.word_tokenize(test_sentence)

# Tag the test sentence using the transformation rule
tagged_test_sentence = apply_transformation_rules([(token, None) for token in test_tokens])

print("Original sentence:")
print(test_sentence)
print("\nTransformed and tagged sentence:")
print(tagged_test_sentence)
