import time
import numpy as np
import matplotlib.pyplot as plt

import algorithm1
import algorithm2
import algorithm3
import algorithm4
import rng_tests

# modify vars
iterations = 100 # Number of times to run RNG tests
n = 100 # sequence length

algorithms = {
    "Park-Miller": algorithm1.park_miller,
    "Middle-Square": algorithm2.middle_square,
    "XORShift": algorithm3.xorshift,
    "HMAC-DRBG": algorithm4.hmac_drbg
}

tests = {
    "Frequency": rng_tests.freq,
    "Runs": rng_tests.runs,
    "Serial": rng_tests.serial
}


def pass_rate(passed, total_iter):
    '''
    Short helper function for computing the pass rate of 
    a given algorithm on a given RNG test.
    '''
    return (passed / total_iter) * 100


# generalized algorithm randomness tester
def test_algo(algorithm, iterations, n):
    results = {name: 0 for name in tests}
    for _ in range(iterations):
        bitstring, _ = algorithm(n)

        for test_name, test_func in tests.items():
            passed = test_func(bitstring)[0]
            if passed:
                results[test_name] += 1
    return results

#generalized run timer (average of many runs - picked 50 to reduce random fluctuation)
def measure_runtime(generator, n, trials=50):
    total = 0

    for _ in range(trials):
        start = time.perf_counter()
        generator(n)
        end = time.perf_counter()
        total += (end - start)

    return total / trials

# pretty print func
def print_results(name, results, runtime, iterations):
    print(f"{name:^30}")
    print("-" * 30)

    for test, passed in results.items():
        rate = pass_rate(passed, iterations)
        print(f"   {test:<12} : {rate:6.1f}%")

    print("-" * 30)
    print(f"{'Average runtime':<12} : {runtime:.6f} s")
    print()

# plot test results func
def plot_tests(results_dict):

    algorithms = list(results_dict.keys())

    frequency = [results_dict[algo]["Frequency"] for algo in algorithms]
    runs = [results_dict[algo]["Runs"] for algo in algorithms]
    serial = [results_dict[algo]["Serial"] for algo in algorithms]

    x = np.arange(len(algorithms))
    width = 0.25

    plt.figure(figsize=(8,5))

    plt.bar(x - width, frequency, width, label="Frequency", color="#1c3144")
    plt.bar(x, runs, width, label="Runs", color="#d00000")
    plt.bar(x + width, serial, width, label="Serial", color="#ffba08")

    plt.xticks(x, algorithms)
    plt.xlabel("Algorithm")
    plt.ylabel("Pass Rate (%)")
    plt.title(f'Randomness Pass Rates of PRNG Algorithms\n(Iterations = {iterations}, Sequence Length = {n})')

    plt.legend(title="Test", loc="center right")
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.show()

# plot runtimes func
def plot_runtime(runtimes_dict):

    algorithms = list(runtimes_dict.keys())
    runtimes = list(runtimes_dict.values())

    plt.figure(figsize=(8,5))

    plt.bar(algorithms, runtimes, color="#78a1bb")

    plt.xlabel("Algorithm")
    plt.ylabel("Average Runtime (s)")
    plt.title(f'Runtimes of PRNG Algorithms\n(Iterations = {iterations}, Sequence Length = {n})')

    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.show()


# main func
def main():
    # store results for plotting
    testresults_dict = {}
    times_dict = {}

    #header
    print()
    print("*********** RESULTS **********")
    print(f"*{f'Iterations: {iterations}':^28}*")
    print(f"*{f'Sequence Length: {n}':^28}*")
    print("*" * 30)
    print()

    # loop over algos
    for name, algorithm in algorithms.items():
        # test randomness + time algo
        results = test_algo(algorithm, iterations, n)
        t = measure_runtime(algorithm, n)

        # add results to dictionaries
        testresults_dict[name] = {
            test: pass_rate(passed, iterations) for test, passed in results.items()
        }
        times_dict[name] = t

        # pretty print test results & runtime for each algo
        print_results(name, results, t, iterations)

    # plots
    plot_tests(testresults_dict)
    plot_runtime(times_dict)




if __name__ == "__main__":
    main()



