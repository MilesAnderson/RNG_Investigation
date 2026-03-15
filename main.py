import time
import numpy as np
import math
import scipy

import algorithm1
import rng_tests
import algorithm2
import algorithm3
import algorithm4

#Tests
iterations = 10000 # Number of times to run RNG tests

def passRate(passed, iter):
    '''
    Short helper function for computing the pass rate of 
    a given algorithm on a given RNG test.
    '''
    return (passed / iter) * 100

#Testing Algorithm 1
alg1_freq_passed = 0
alg1_runs_passed = 0
for _ in range(iterations):
    alg1_bitString, _ = algorithm1.Random(10)
    alg1_freq_isRand, _ = rng_tests.freq_test(alg1_bitString)
    alg1_runs_isRand, _ = rng_tests.runs(alg1_bitString)
    if (alg1_freq_isRand == True):
        alg1_freq_passed += 1
    if (alg1_runs_isRand == True):
        alg1_runs_passed += 1
print("algorithm 1 is random per frequency test: ", passRate(alg1_freq_passed, iterations), "%", " of the time")
print("algorithm 1 is random per runs test: ", passRate(alg1_runs_passed, iterations), "%", " of the time")
print()

#Testing Algorithm 2
alg2_freq_passed = 0
alg2_runs_passed = 0
for _ in range(iterations):
    alg2_bitString, _ = algorithm2.middle_square(10)
    alg2_freq_isRand, _ = rng_tests.freq_test(alg2_bitString)
    alg2_runs_isRand, _ = rng_tests.runs(alg2_bitString)
    if (alg2_freq_isRand == True):
        alg2_freq_passed += 1
    if (alg2_runs_isRand == True):
        alg2_runs_passed += 1
print("algorithm 2 is random per frequency test: ", passRate(alg2_freq_passed, iterations), "%", " of the time")
print("algorithm 2 is random per runs test: ", passRate(alg2_runs_passed, iterations), "%", " of the time")
print()

#Testing Algorithm 3
alg3_freq_passed = 0
alg3_runs_passed = 0
for _ in range(iterations):
    alg3_bitString, _ = algorithm3.xorshift(10)
    alg3_freq_isRand, _ = rng_tests.freq_test(alg3_bitString)
    alg3_runs_isRand, _ = rng_tests.runs(alg3_bitString)
    if (alg3_freq_isRand == True):
        alg3_freq_passed += 1
    if (alg3_runs_isRand == True):
        alg3_runs_passed += 1
print("algorithm 3 is random per frequency test: ", passRate(alg3_freq_passed, iterations), "%", " of the time")
print("algorithm 3 is random per runs test: ", passRate(alg3_runs_passed, iterations), "%", " of the time")
print()

#Testing Algorithm 4
alg4_freq_passed = 0
alg4_runs_passed = 0
for _ in range(iterations):
    alg4_bitString, _ = algorithm4.hmac_drbg(10)
    alg4_freq_isRand, _ = rng_tests.freq_test(alg4_bitString)
    alg4_runs_isRand, _ = rng_tests.runs(alg4_bitString)
    if(alg4_freq_isRand == True):
        alg4_freq_passed += 1
    if(alg4_runs_isRand == True):
        alg4_runs_passed += 1
print("algorithm 4 is random per frequency test: ", passRate(alg4_freq_passed, iterations), "%", " of the time")
print("algorithm 4 is random per runs test: ", passRate(alg4_runs_passed, iterations), "%", " of the time")
print()



#Timing
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

start = time.time()
algorithm3.xorshift(1000)
end = time.time()
alg3_time = end - start
print("Algorithm 3 time: ", alg3_time)

start = time.time()
algorithm4.hmac_drbg(1000)
end = time.time()
alg4_time = end - start
print("Algorithm 4 time: ", alg4_time)

