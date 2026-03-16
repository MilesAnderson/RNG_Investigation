import random
import hashlib
import hmac

def hmac_drbg(n):
    """
    Generates n values using an HMAC-DRBG pseudo-random number generator
    based on SHA-256.

    Starting from an initial random seed, the algorithm maintains an internal
    state consisting of a key and value block. Each step updates this state
    using HMAC-SHA256 and produces a new 256-bit pseudo-random value. The
    function returns both the generated integers and a concatenated binary
    representation of those values.
    """
    # Step 1: create an initial random seed (32 bytes)
    seed_int = random.getrandbits(256)
    seed = seed_int.to_bytes(32, byteorder='big')

    # Step 2: initialize state
    K = b'\x00' * 32
    V = b'\x01' * 32

    def hmac_sha256(key, data):
        return hmac.new(key, data, hashlib.sha256).digest()

    def update(provided_data=b''):
        nonlocal K, V
        K = hmac_sha256(K, V + b'\x00' + provided_data)
        V = hmac_sha256(K, V)

        if provided_data != b'':
            K = hmac_sha256(K, V + b'\x01' + provided_data)
            V = hmac_sha256(K, V)

    # Step 3: seed the generator
    update(seed)

    # Step 4: generate output
    bits = ""
    ret = []

    for _ in range(n):
        V = hmac_sha256(K, V)
        value = int.from_bytes(V, byteorder='big')
        ret.append(value)

        bits += format(value, '0256b') # 256 bits for SHA256

    return bits, ret