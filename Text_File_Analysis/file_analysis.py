import os
import sys
import re

# File name
file = sys.argv[1]

res = {
    "total_lines":"",
    "total_characters":"",
    "total_words":"",
    "unique_words":"",
    "special_characters":""
}


# Data lists
words = []
chars = []

# Open text file
with open(file, 'r') as f:
    # Read lines
    lines = f.readlines()
    res['total_lines'] = len(lines)

    # Remove any punctiations from each line like ['!', '.', '?', etc..]
    # Append words to the list
    for line in lines:
        content = re.sub(r'[^\w\s]','',line)
        words += content.split()

    res['total_words'] = len(words)

    unique_words = set(words)
    res['unique_words'] = len(unique_words)

    for word in words:
        chars += list(word)
    res['total_characters'] = len(chars)

    special_chars = set(chars)
    res['special_characters'] = len(special_chars)

    print(res)