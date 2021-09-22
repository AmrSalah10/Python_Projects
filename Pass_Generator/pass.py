import string
import random

length = 16
sequence = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.sample(sequence, length))


print(string.ascii_letters)

