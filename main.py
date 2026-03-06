import time
import numpy as np
import math
import scipy

import algorithm1
import rng_tests

'''
#time Random
start = time.time()
algorithm1.Random(1000)
end = time.time()
alg1_time = end - start

print(alg1_time)
'''

print(algorithm1.Random(5))

isRandom, p_value = rng_tests.freq_test(algorithm1.Random(100))
print(isRandom)
print(p_value)
