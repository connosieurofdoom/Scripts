# Spelling Corrector
# pip install pyspellchecker
from spellchecker import SpellChecker
tool = SpellChecker()
word = input("Enter a word: ")
word = word.lower()
if word in tool:
    print("The word is correct.")
else:
    correction = tool.correction(word)
    print(f"The word is incorrect. Did you mean {correction}?")