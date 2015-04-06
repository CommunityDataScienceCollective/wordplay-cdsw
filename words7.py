import re
import scrabble

pattern = re.compile("unmois")
for word in scrabble.wordlist:
    if pattern.search(word):
        print(word)
