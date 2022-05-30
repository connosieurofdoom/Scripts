# Grammer Corrector
# Method 1
# pip install grammar-check
from grammar_check import LanguageTool
def grammar_check(text):
    lt = LanguageTool('en-US')
    matches = lt.check(text)
    return matches
# Method 2
# pip install gingerit
import gingerit
def ginger_check(text):
    gi = gingerit.GingerIt()
    return gi.parse(text)