import json
from difflib import get_close_matches


def findDefinition(dictionary, word):
    word = word.lower()
    close_match = get_close_matches(word, dictionary.keys(), n=1, cutoff=0.8)

    if len(close_match) == 0:
        return f"The word {word} was not found in the dictionary."
    else:
        if word == close_match[0]:
            return dictionary[word]
        else:
            print(f"Did you mean {close_match[0]}?")
            answer = input("[yes/no]\n")
        
            if answer == "yes":
                return dictionary[close_match[0]]
            elif answer == "no":
                return f"The word {word} was not found in the dictionary."
            else:
                return "The answer is not correct."


if __name__ == "__main__":
    with open("data.json") as file:
        dictionary = json.load(file)
    word = input("Enter word: ")
    
    definitions = findDefinition(dictionary, word)

    # we can either receive a list of definitions
    # or one of the possible communicates
    if isinstance(definitions, list):
        for actDef in definitions:
            print(actDef)
    else:
        print(definitions)