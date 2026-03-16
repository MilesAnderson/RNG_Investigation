import numpy as np
import math
from scipy import special
from collections import Counter
from scipy.special import gammaincc

def floatList_to_binaryString(x):
    """
    Converts a list of floating-point values into a concatenated binary string.

    Each value is cast to a 32-bit float and replaced by its IEEE 754 binary
    representation. The resulting 32-bit strings are concatenated and returned
    as a single binary sequence.
    """
    binary_string = []
    for i in range (len(x)):
        binary_string.append(np.binary_repr(np.float32(x[i]).view(np.int32)))
    binary_string = "".join(map(str, binary_string))
    return binary_string

def freq_test(binaryString):
    """
    Performs a monobit frequency test on a binary string.

    The test counts the difference between the number of ones and zeros in the
    input sequence and uses the complementary error function to compute a p-value.
    It returns whether the sequence passes the test at the 0.01 significance level
    and the corresponding p-value.
    """
    binary_string = binaryString

    S_n = 0
    n = len(binary_string)
    for i in range (n):
        if (binary_string[i] == '1'):
            S_n = S_n + 1
        else:
            S_n = S_n - 1

    s_obs = abs(S_n) / math.sqrt(n)

    P_value = special.erfc(s_obs / math.sqrt(2))

    isRandom = True
    if (P_value < 0.01):
        isRandom = False

    return isRandom, P_value

def runs(binaryString):
    """
    Performs a runs test on a binary string.

    The test measures the total number of runs, or transitions between consecutive
    bits, and compares the observed count to the expected count based on the
    proportion of ones in the sequence. It returns whether the sequence passes
    the test at the 0.01 significance level and the corresponding p-value.
    """
    binary_string = binaryString
    n = len(binary_string)

    if n == 0:
        return False, 0

    ones = 0
    for i in range (n):
        if (binary_string[i] == '1'):
            ones = ones + 1
    pi = ones / n

    if pi == 0 or pi == 1:
        return False, 0

    tau = 2 / math.sqrt(n)
    if (abs(pi - (1 / 2)) >= tau):
        return False, 0

    V_n = 1
    for i in range (n-1):
        if (binary_string[i] != binary_string[i+1]):
            V_n = V_n + 1

    numerator = V_n - (2 * n * pi * (1 - pi))
    denominator = 2 * math.sqrt(2 * n) * pi * (1 - pi)

    p_value = special.erfc(abs(numerator) / denominator)

    isRandom = True
    if (p_value < 0.01):
        isRandom = False

    return isRandom, p_value

def serial(binaryString, m=3):
    """
    Performs a serial test on a binary string.

    The test examines the frequency of overlapping bit patterns of length m in the
    input sequence and compares the observed distribution to the expected uniform
    distribution. Two statistics are computed based on the counts of patterns of
    length m, m-1, and m-2, and corresponding p-values are calculated.

    The function returns whether the sequence passes the test at the 0.01
    ignificance level along with the two p-values.
    """
    n = len(binaryString)

    if n < m or m < 2:
        return False, 0.0, 0.0
    
    extended = binaryString + binaryString[:m - 1]

    def psi2(sequence, block_size):
        if block_size <= 0:
            return 0.0

        counts = Counter()
        for i in range(n):
            pattern = sequence[i:i + block_size]
            counts[pattern] += 1

        total = 0
        for count in counts.values():
            total += count * count

        return (total * (2 ** block_size) / n) - n

    psi_m   = psi2(extended, m)
    psi_m1  = psi2(extended, m - 1)
    psi_m2  = psi2(extended, m - 2)

    delta1 = psi_m - psi_m1
    delta2 = psi_m - (2 * psi_m1) + psi_m2

    p_value1 = gammaincc(2 ** (m - 2), delta1 / 2.0)
    p_value2 = gammaincc(2 ** (m - 3), delta2 / 2.0)

    isRandom = (p_value1 >= 0.01) and (p_value2 >= 0.01)

    return isRandom, p_value1, p_value2
    
