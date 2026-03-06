import time
import numpy as np
import math
import scipy

import algorithm1
import freq_test

'''
#time Random
start = time.time()
algorithm1.Random(1000)
end = time.time()
alg1_time = end - start

print(alg1_time)
'''

x = algorithm1.Random(1000000)
isRand, p_value = freq_test.freq_test(x)
print(isRand)
print(p_value)
