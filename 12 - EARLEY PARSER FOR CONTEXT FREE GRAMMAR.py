class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.chart = []

    def parse(self, input_string):
        self.chart = [[] for _ in range(len(input_string) + 1)]

        self.predict(0, "S", 0)
        self.parse_input(input_string)

        if self.accepts("S", 0, len(input_string)):
            print("Parsing successful.")
        else:
            print("Parsing failed.")

    def predict(self, column, symbol, dot_position):
        for production in self.grammar.get(symbol, []):
            self.chart[column].append((symbol, production, dot_position))

    def scan(self, column, symbol, dot_position, input_string):
        for production in self.grammar[symbol]:
            if dot_position < len(production) and production[dot_position] == input_string[column]:
                self.chart[column + 1].append((symbol, dot_position + 1, dot_position + 1))

    def complete(self, column, symbol, dot_position):
        for entry in self.chart[column]:
            _, _, entry_dot_position = entry
            if entry_dot_position == dot_position and entry[1] < len(self.grammar[entry[0]][0]):
                self.predict(column, entry[0], entry[1])

    def parse_input(self, input_string):
        for column in range(len(input_string) + 1):
            for entry in self.chart[column]:
                symbol, dot_position, start_column = entry
                if dot_position == len(self.grammar[symbol][0]):
                    self.complete(column, symbol, start_column)
                elif symbol in self.grammar:
                    self.scan(column, symbol, dot_position, input_string)
                else:
                    self.predict(column, symbol, dot_position)

    def accepts(self, symbol, dot_position, end_column):
        return (symbol, dot_position, 0) in self.chart[end_column]


# Example usage
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": ["the", "a"],
    "N": ["cat", "dog", "bat"],
    "V": ["chased", "ate"]
}

parser = EarleyParser(grammar)
parser.parse("the cat chased the dog")
