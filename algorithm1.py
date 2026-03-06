
import random

def Random(n):
    i = 1.0
    k = 16807
    j = 2147483647
    seed = random.randint(1, j)
    bits = ""
    while i <= n:
        seed = (k * seed) % j
        bits += format(seed, '031b')
        i = i+1
    return bits
    
