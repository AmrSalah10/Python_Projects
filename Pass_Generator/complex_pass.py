import random
import string


alpha = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

alpha_len = 8
num_len = 5
sym_len = 3


def pass_generator(sequence, length):
    Pass = ''
    if sequence == alpha:
        for i in range(length):
            index = random.randint(0, len(sequence) - 1)
            case = random.randint(0,1)
            if case == 1:
                Pass += sequence[index].upper()
            else:
                Pass += sequence[index]
    Pass += ''.join(random.sample(sequence, length))
    return Pass

password = pass_generator(alpha, alpha_len)
password += pass_generator(numbers, num_len) 
password += pass_generator(symbols, sym_len) 

print(password)
    




