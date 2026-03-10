import time
import numpy as np
import math
import scipy

import algorithm1
import rng_tests
import algorithm2

#Tests
'''
Note: I'm thinking a better way of doing the tests is doing abunch of them
and then displaying the percentage of the times a given algorithms passes
the test. 
'''
alg1_freq_passed = 0
alg1_runs_passed = 0
for _ in range(100):
    alg1_bitString, _ = algorithm1.Random(10)
    alg1_freq_isRand, _ = rng_tests.freq_test(alg1_bitString)
    alg1_runs_isRand, _ = rng_tests.runs(alg1_bitString)
    if (alg1_freq_isRand == True):
        alg1_freq_passed += 1
    if (alg1_runs_isRand == True):
        alg1_runs_passed += 1
print("algorithm 1 is random per frequency test: ", alg1_freq_passed, "%", " of the time")
print("algorithm 1 is random per runs test: ", alg1_runs_passed, "%", " of the time")
print()

alg2_freq_passed = 0
alg2_runs_passed = 0
for _ in range(100):
    alg2_bitString, _ = algorithm2.middle_square(10)
    alg2_freq_isRand, _ = rng_tests.freq_test(alg2_bitString)
    alg2_runs_isRand, _ = rng_tests.runs(alg2_bitString)
    if (alg2_freq_isRand == True):
        alg2_freq_passed += 1
    if (alg2_runs_isRand == True):
        alg2_runs_passed += 1
print("algorithm 2 is random per frequency test: ", alg2_freq_passed, "%", " of the time")
print("algorithm 2 is random per runs test: ", alg2_runs_passed, "%", " of the time")



#Timing
print()
start = time.time()
algorithm1.Random(1000)
end = time.time()
alg1_time = end - start
print("Algorithm 1 time: ", alg1_time)

start = time.time()
algorithm2.middle_square(1000)
end = time.time()
alg2_time = end - start
print("Algorithm 2 time: ", alg2_time)

