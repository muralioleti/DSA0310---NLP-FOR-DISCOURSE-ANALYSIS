class PluralGeneratorFSM:
    def __init__(self):
        # Define states
        self.states = {'q0', 'q1', 'q2'}
        
        # Define alphabet
        self.alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                         'u', 'v', 'w', 'x', 'y', 'z'}
        
        # Define transitions
        self.transitions = {
            'q0': {'consonant': 'q1', 'vowel': 'q2'},
            'q1': {'consonant': 'q1', 'vowel': 'q2'},
            'q2': {'consonant': 'q1', 'vowel': 'q2'}
        }
        
        # Set initial state
        self.current_state = 'q0'
    
    def process_input(self, input_string):
        # Process input string and update current state
        for char in input_string:
            if char.lower() in self.alphabet:
                if char.lower() in {'a', 'e', 'i', 'o', 'u'}:
                    category = 'vowel'
                else:
                    category = 'consonant'
                self.current_state = self.transitions[self.current_state][category]
        
        # Generate plural form based on the final state
        if self.current_state == 'q1':
            plural_form = input_string + 's'
        else:
            plural_form = input_string + 'es'
        
        return plural_form

# Example usage
plural_generator = PluralGeneratorFSM()

# Test with different nouns
input_noun1 = "cat"
plural1 = plural_generator.process_input(input_noun1)
print(f"The plural form of '{input_noun1}' is '{plural1}'")

input_noun2 = "dog"
plural2 = plural_generator.process_input(input_noun2)
print(f"The plural form of '{input_noun2}' is '{plural2}'")

input_noun3 = "fish"
plural3 = plural_generator.process_input(input_noun3)
print(f"The plural form of '{input_noun3}' is '{plural3}'")
