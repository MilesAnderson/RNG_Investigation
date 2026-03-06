
import random

def Random(n):
    i = 1.0
    x = []
    k = 16807
    j = 2147483647
    seed = random.randint(1, j)
    while i <= n:
        seed = (k * seed) % j
        x.append(seed / j)
        i = i+1
    return x
    
