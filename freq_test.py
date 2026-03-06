import numpy as np
import math
from scipy import special

def freq_test(x):
    binary_string = []
    for i in range (len(x)):
        binary_string.append(np.binary_repr(np.float32(x[i]).view(np.int32)))
    binary_string = "".join(map(str, binary_string))

    S_n = 0
    n = len(binary_string)
    for i in range (n):
        if (binary_string[i] == '1'):
            S_n = S_n + 1
        else:
            S_n = S_n - 1

    s_obs = abs(S_n) / math.sqrt(n)

    P_value = special.erfc(s_obs / math.sqrt(abs(S_n)))

    isRandom = True
    if (P_value < 0.01):
        isRandom = False

    return isRandom, P_value



    

    
