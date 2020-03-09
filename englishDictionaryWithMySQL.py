import mysql.connector
from difflib import get_close_matches


def findDefinition(dictionaryCursor, word):
    word = word.capitalize()

    query = dictionaryCursor.execute(f"SELECT definition FROM Entries WHERE word = '{word}'")
    results = cursor.fetchall()

    if results:
        return results
    else:
        # we're looking for similar words in the dictionary
        query = dictionaryCursor.execute("SELECT word FROM Entries")
        words = [actWord[0] for actWord in cursor.fetchall()]
        closeMatch = get_close_matches(word, words, n=1, cutoff=0.8)

        if len(closeMatch) == 0:
            return f"The word {word} was not found in the dictionary."
        else:
            print(f"Did you mean {closeMatch[0]}?")
            answer = input("[yes/no]\n")
        
            if answer == "yes":
                query = dictionaryCursor.execute(f"SELECT definition FROM Entries WHERE word = '{closeMatch[0]}'")
                results = cursor.fetchall()
                return results
            elif answer == "no":
                return f"The word {word} was not found in the dictionary."
            else:
                return "The answer is not correct."


if __name__ == "__main__":
    # first we establish connection to the MySQL dictionary database
    dictionaryConnection = mysql.connector.connect(
        host = "localhost",
        database = "entries",
        user = "root",
        password = "mariusz"
    )
    cursor = dictionaryConnection.cursor()

    word = input("Enter word: ")
    definitions = findDefinition(cursor, word)

    # we can either receive a list of definitions
    # or one of the possible communicates
    if isinstance(definitions, list):
        for actDef in definitions:
            print(actDef[0])
    else:
        print(definitions)
