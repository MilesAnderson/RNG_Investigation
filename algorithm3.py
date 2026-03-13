import random

def xorshift(n):
    ret = []
    bits = ""
    for _ in range (n):
        seed = random.randint(1, 2147483647)
        seed ^= seed << 13
        seed ^= seed >> 17
        seed ^= seed << 5
        width = seed.bit_length()
        bits += format(seed, f'0{width}b')
        ret.append(seed)

    return bits, ret
