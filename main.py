import time
import numpy as np
import math
import scipy

import algorithm1
import rng_tests
import algorithm2

'''
#time Random
start = time.time()
algorithm1.Random(1000)
end = time.time()
alg1_time = end - start

print(alg1_time)
'''

bit_string, _ = algorithm2.middle_square(50)
print(bit_string)
print(_)
print(rng_tests.freq_test(bit_string))
print(rng_tests.runs(bit_string))
