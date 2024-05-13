import json
import difflib

# Download the JSON data from the link and save it as 'data.json'
# Load JSON data into a Python dictionary
with open('data.json') as f:
    data = json.load(f)

def get_definition(word):
    # Check if the word is in the dictionary
    word = word.lower()
    if word in data:
        return data[word]
    else:
        # If the word is not in the dictionary, suggest a similar word
        suggestions = difflib.get_close_matches(word, data.keys(), n=1)
        if suggestions:
            suggestion = suggestions[0]
            yn = input(f"Did you mean '{suggestion}' instead? Enter Y if yes, or N if no: ").lower()
            if yn == 'y':
                return data[suggestion]
            else:
                return "The word doesn't exist. Please double check it."
        else:
            return "The word doesn't exist. Please double check it."

# Test the function
word = input("Enter a word: ")
print(get_definition(word))
