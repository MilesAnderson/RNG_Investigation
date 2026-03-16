import random

def xorshift(n):
    """
    Generates n pseudo-random numbers using the XORShift generator.

    Random seed is chosen between 1 and 2^31 - 1, then each iteration applies
    a sequence of XOR and bit-shift operations to produce the next value in the
    sequence. The function returns both the generated integers and a concatenated
    binary representation of those values.
    """
    ret = []
    bits = ""
    seed = random.randint(1, 2147483647)

    for _ in range (n):
        seed ^= seed << 13
        seed ^= seed >> 17
        seed ^= seed << 5

        seed &= 0xffffffff # mask seed to 32 bits

        bits += format(seed, '032b') # 32 bit width
        ret.append(seed)

    return bits, ret
