import re

def pattern_matcher(pattern, text):
    """
    Function to demonstrate pattern matching using regular expressions.
    
    Parameters:
    - pattern: The regular expression pattern to search for.
    - text: The text in which to search for the pattern.
    """
    # Use re.match() to check if the pattern matches at the beginning of the text
    match_at_start = re.match(pattern, text)
    
    # Use re.search() to search for the pattern anywhere in the text
    match_anywhere = re.search(pattern, text)
    
    # Use re.findall() to find all occurrences of the pattern in the text
    all_occurrences = re.findall(pattern, text)
    
    # Print the results
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    
    if match_at_start:
        print("Match at the beginning of the text.")
    else:
        print("No match at the beginning of the text.")
        
    if match_anywhere:
        print("Match found anywhere in the text.")
    else:
        print("No match found anywhere in the text.")
        
    if all_occurrences:
        print(f"All occurrences of the pattern: {all_occurrences}")
    else:
        print("No occurrences found in the text.")
    
# Example usage
pattern = r'^[A-Za-z]+\d+$'  # Matches words followed by digits at the end of the line
text_to_search = "Hello123"

pattern_matcher(pattern, text_to_search)
