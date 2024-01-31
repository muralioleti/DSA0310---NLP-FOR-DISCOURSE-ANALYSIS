import re

def parse_fopc(expression):
    # Define a simple grammar for FOPC expressions
    pattern = re.compile(r'\s*([\w\d]+)\s*([=!<>]+)\s*([\w\d]+)\s*')

    # Match the pattern
    match = pattern.match(expression)

    if match:
        # Extract components
        left_operand = match.group(1)
        operator = match.group(2)
        right_operand = match.group(3)

        # Construct a simple representation of the expression
        return {
            'left_operand': left_operand,
            'operator': operator,
            'right_operand': right_operand
        }
    else:
        return None

# Example usage
logical_expression = "x = y"
parsed_expression = parse_fopc(logical_expression)

if parsed_expression:
    print("Parsed Expression:", parsed_expression)
else:
    print("Invalid logical expression.")
