import numpy as np
import math
from scipy import special

def floatList_to_binaryString(x):
    binary_string = []
    for i in range (len(x)):
        binary_string.append(np.binary_repr(np.float32(x[i]).view(np.int32)))
    binary_string = "".join(map(str, binary_string))
    return binary_string

def freq_test(floatList):
    binary_string = floatList

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

def runs(floatList):
    binary_string = floatList
    n = len(binary_string)

    ones = 0
    for i in range (n):
        if (binary_string[i] == '1'):
            ones = ones + 1
    pi = ones / n

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
    


    

    
