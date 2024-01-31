import random

def train_probabilistic_model():
    # This is a simple hardcoded probabilistic model for demonstration purposes.
    # In practice, you would train the model on a larger corpus.
    model = {
        'The': {'DET': 0.9, 'NOUN': 0.1},
        'cat': {'NOUN': 0.8, 'VERB': 0.2},
        'is': {'VERB': 0.9, 'ADV': 0.1},
        'on': {'ADP': 0.7, 'NOUN': 0.3},
        'the': {'DET': 0.8, 'ADJ': 0.2},
        'mat': {'NOUN': 0.6, 'VERB': 0.4}
        # Add more words and their corresponding probabilities as needed
    }
    return model

def stochastic_pos_tagging(sentence, probabilistic_model):
    words = sentence.split()
    tagged_sentence = []

    for word in words:
        if word in probabilistic_model:
            pos_tags = list(probabilistic_model[word].keys())
            probabilities = list(probabilistic_model[word].values())
            chosen_tag = random.choices(pos_tags, probabilities)[0]
            tagged_sentence.append((word, chosen_tag))
        else:
            # If the word is not in the model, default to a generic tag (e.g., 'NOUN')
            tagged_sentence.append((word, 'NOUN'))

    return tagged_sentence

# Example usage
sentence_to_tag = "The cat is on the mat"
probabilistic_model = train_probabilistic_model()

tagged_sentence = stochastic_pos_tagging(sentence_to_tag, probabilistic_model)

print("Original sentence:")
print(sentence_to_tag)
print("\nStochastic POS-tagged sentence:")
print(tagged_sentence)
