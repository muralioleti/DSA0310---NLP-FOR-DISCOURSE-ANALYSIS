class EndsWithABAutomaton:
    def __init__(self):
        # Define states
        self.states = {'q0', 'q1', 'q2'}
        
        # Define alphabet
        self.alphabet = {'a', 'b'}
        
        # Define transitions
        self.transitions = {
            'q0': {'a': 'q0', 'b': 'q1'},
            'q1': {'a': 'q0', 'b': 'q2'},
            'q2': {'a': 'q0', 'b': 'q1'}
        }
        
        # Set initial state
        self.current_state = 'q0'
        
        # Set accepting state
        self.accepting_state = 'q2'
    
    def process_input(self, input_string):
        # Process input string and update current state
        for symbol in input_string:
            if symbol not in self.alphabet:
                print(f"Invalid symbol '{symbol}' encountered. Exiting.")
                return False
            self.current_state = self.transitions[self.current_state][symbol]
        
        # Check if the final state is the accepting state
        if self.current_state == self.accepting_state:
            print(f"The string '{input_string}' ends with 'ab'.")
            return True
        else:
            print(f"The string '{input_string}' does not end with 'ab'.")
            return False

# Example usage
automaton = EndsWithABAutomaton()

# Test with different strings
automaton.process_input("aaaab")  # Should print "The string 'aaaab' ends with 'ab'."
automaton.process_input("ab")    # Should print "The string 'ab' ends with 'ab'."
automaton.process_input("abc")   # Should print "The string 'abc' does not end with 'ab'."
automaton.process_input("a")     # Should print "The string 'a' does not end with 'ab'."
