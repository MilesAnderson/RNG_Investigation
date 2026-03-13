import random

def xorshift():
    bits = ""

    seed = random.randint(1, 2147483647)
    seed ^= seed << 13
    seed ^= seed >> 17
    seed ^= seed << 5

    width = seed.bit_length()
    bits += format(seed, f'0{width}b')

    return bits

print(xorshift())