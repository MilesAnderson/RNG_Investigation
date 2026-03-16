
import random

def park_miller(n):
    """
    Generates n pseudo-random numbers using the Park–Miller linear congruential generator.
    
    Each iteration computes seed = (16807 * seed) % 2147483647 to produce a
    pseudo-random sequence. The function returns both the concatenated 31-bit
    binary representation of each generated value and the normalized values
    (seed / 2147483647) in the interval (0,1).
    """
    i = 1.0
    x = []
    k = 16807
    j = 2147483647
    seed = random.randint(1, j)
    bits = ""
    while i <= n:
        seed = (k * seed) % j

        bits += format(seed, '031b') # 31 bit width for numbers between 0 and 2^31-1
        x.append(seed / j)
        i += 1
    return bits, x
    
