import random

def xorshift(n):
    """
    Generates n pseudo-random numbers using the XORShift generator.

    Each iteration begins with a random seed between 1 and 2^31 − 1 and applies
    a sequence of XOR and bit-shift operations to produce the next value in the
    sequence. The function returns both the generated integers and a concatenated
    binary representation of those values.
    """
    ret = []
    bits = ""
    for _ in range (n):
        seed = random.randint(1, 2147483647)
        seed ^= seed << 13
        seed ^= seed >> 17
        seed ^= seed << 5
        # width = seed.bit_length()
        # bits += format(seed, f'0{width}b')
        bits += format(seed, '031b') # 31 bit width for numbers between 0 and 2^31-1
        ret.append(seed)

    return bits, ret
