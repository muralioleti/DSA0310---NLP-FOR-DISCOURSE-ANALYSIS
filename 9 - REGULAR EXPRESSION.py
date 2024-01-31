import re

def rule_based_pos_tagging(sentence):
    tagged_sentence = []
    
    for word in sentence.split():
        if re.match(r'\b(?:The|A|An)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'DET'))
        elif re.match(r'\b(?:is|am|are|was|were)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'VERB'))
        elif re.match(r'\b(?:cat|dog|mat)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'NOUN'))
        elif re.match(r'\b(?:on|in|under)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'PREP'))
        elif re.match(r'\b(?:quick|lazy|brown)\b', word, re.IGNORECASE):
            tagged_sentence.append((word, 'ADJ'))
        else:
            tagged_sentence.append((word, 'NOUN'))  # Default to 'NOUN' if no match is found
    
    return tagged_sentence

# Example usage
sentence_to_tag = "The quick brown cat is on the mat"
tagged_sentence = rule_based_pos_tagging(sentence_to_tag)

print("Original sentence:")
print(sentence_to_tag)
print("\nRule-based POS-tagged sentence:")
print(tagged_sentence)
