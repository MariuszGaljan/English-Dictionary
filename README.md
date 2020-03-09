# English-Dictionary
An app providing definitions of given english words

**Written in Python**

When given a word, the program searches the dictionary for its definition.
If the word is found, the definition is printed.
Else the program searches for any similar words and chooses the closest one. Then it asks the user if that was the searched word.
If it doesn't find any similar word or the user did not mean the suggestion, the app prints a communicate that the word was not found.

## Launching the program

There are two version of this application. One is using the included json file as the dictionary, the other is using a MySQL database (which you can create locally using the given SQL script).

The program requires installing the MySQL module.

## What I learned
* How to parse json files using the Python **built-in json library**
* How to access the MySQL database using the **mysql.connector module**
* How to use the Python **difflib library** to search for similar words in the given lists or strings
