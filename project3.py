#Problem 3 - Combinations

import math

def combo(numberOfSocks, pairs):
    final = math.factorial(pairs) / (math.factorial(pairs-numberOfSocks) * math.factorial(numberOfSocks))
    print(str(final))

number = 2
pairs = int(input("Enter the number of socks: "))

combo(number, pairs)
