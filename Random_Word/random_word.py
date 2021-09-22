# Pick up random word from text file
import sys
import random

file = 'text.txt'
with open(file, 'r') as f:
    text = f.read()
    words = text.split()
    print(random.choice(words))


