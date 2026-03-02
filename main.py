import time

import algorithm1

start = time.time()
algorithm1.algorithm1(32545, 1000)
end = time.time()
alg1_time = end - start

print("Algorithm1 run time: ", alg1_time)