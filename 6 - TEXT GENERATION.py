import random

def generate_bigram_model(text):
    words = text.split()
    bigram_model = {}
    
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        
        if current_word not in bigram_model:
            bigram_model[current_word] = [next_word]
        else:
            bigram_model[current_word].append(next_word)
    
    return bigram_model

def generate_text(bigram_model, length=10, seed=None):
    if seed:
        random.seed(seed)
    
    current_word = random.choice(list(bigram_model.keys()))
    generated_text = [current_word]
    
    for _ in range(length - 1):
        if current_word in bigram_model:
            next_word = random.choice(bigram_model[current_word])
            generated_text.append(next_word)
            current_word = next_word
        else:
            break
    
    return ' '.join(generated_text)

# Example usage
text_corpus = "This is a sample text for the bigram model. It generates text based on the probability of the next word given the current word."
bigram_model = generate_bigram_model(text_corpus)

generated_text = generate_text(bigram_model, length=15, seed=42)
print(generated_text)
