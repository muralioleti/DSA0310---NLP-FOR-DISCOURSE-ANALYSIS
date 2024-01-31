class SimpleParser:
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, input_string):
        self.tokens = input_string.split()
        self.current_token_index = 0

        try:
            self.parse_s()
            print("Parsing successful.")
        except ParseError as e:
            print(f"Parsing error: {e}")

    def match(self, expected_token):
        if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index] == expected_token:
            self.current_token_index += 1
        else:
            raise ParseError(f"Expected '{expected_token}' but found '{self.tokens[self.current_token_index]}'")

    def parse_s(self):
        self.match("if")
        self.parse_condition()
        self.match("then")
        self.parse_s()

    def parse_condition(self):
        self.match("(")
        self.parse_expression()
        self.match(")")

    def parse_expression(self):
        self.match("id")
        self.match("op")
        self.match("id")


class ParseError(Exception):
    pass


# Example usage
grammar = """
S -> if C then S
C -> (E)
E -> id op id
"""

parser = SimpleParser(grammar)
parser.parse("if (x + y) then if (z * w) then id op a")
