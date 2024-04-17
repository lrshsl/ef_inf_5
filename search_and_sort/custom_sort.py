import sys
from random import randint
from time import perf_counter


def bubble_sort(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort_custom(arr: list) -> list:
    for i in range(1, len(arr)):
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr


def insertion_sort(arr: list) -> list:
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


def shell_sort_custom(arr: list) -> list:
    j = len(arr) // 2
    while j > 0:
        for i in range(len(arr) // 2):
            if arr[i] > arr[i + j]:
                arr[i], arr[i + j] = arr[i + j], arr[i]
        j //= 2
    return arr


def shell_sort(array):

    # Distance between the elements (len(arr) // 2, len(arr) // 4, .. 1)
    j = len(array) // 2

    while j > 0:

        # Step through half/quarter/eighth.. of the array
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


def radix_sort_custom(arr: list, z: int = 1) -> list:
    buckets = [list() for _ in range(10)]
    for n in arr:
        buckets[(n // z) % 10].append(n)
    if len(buckets[0]) != len(arr):     # Problem when all numbers have 0 at the same digit
        return radix_sort_custom([e
                                  for buc in buckets
                                  for e in buc], z * 10)
    return arr

def radix_sort_without_recursion(arr: list) -> list:
    max_digits = max(arr).__str__().__len__()
    z: int = 1
    for _ in range(max_digits):
        buckets: list = [list() for _ in range(10)]
        for n in arr:
            buckets[(n // z) % 10].append(n)
        z *= 10
    return arr


def run_benchmark(fn, max_exponent=6, max_element=100000, repetitions=100):
    for n in range(1, max_exponent + 1):
        n_elements = 10**n
        arr = [randint(0, max_element) for _ in range(n_elements)]
        start = perf_counter()
        for _ in range(repetitions):
            fn(arr)
        end = perf_counter()
        print("\t{} elements: {}s".format(n_elements, (end - start)))


def test_all(funcs: list, max_exponent=4, max_element=1000):
    for n in range(1, max_exponent + 1):
        n_elements = 10**n
        arr = [randint(0, max_element) for _ in range(n_elements)]
        sorted_arr = sorted(arr)
        for fn in funcs:
            if fn(arr) == sorted_arr:
                print(f"{fn.__name__} test passed for n = {n},\n elements = {n_elements}\n max_element = {max_element}")
            else:
                print(fn(arr))

def main():
    max_exponent = 4
    max_element = 1_000
    algs = [
        # bubble_sort,
        insertion_sort_custom,
        insertion_sort,
        shell_sort_custom,
        radix_sort_custom,
    ]

    if len(sys.argv) == 2:
        if sys.argv[1].isnumeric():
            max_exponent = int(sys.argv[1])
        elif sys.argv[1] in ("t", "test", "testall"):
            test_all(algs)
            return
    elif len(sys.argv) == 3:
        max_exponent = int(sys.argv[1])
        max_element = int(sys.argv[2])

    test_arr = [randint(0, 100) for _ in range(10)]

    longest_name = max([len(alg.__name__) for alg in algs])
    for alg in algs:
        print("\nBenchmarking fn {}:".format(alg.__name__) + " " * (longest_name - len(alg.__name__)), end="\t\t\t")
        alg_result, expected_result = alg(test_arr), sorted(test_arr)
        is_correct = alg_result == expected_result
        if not is_correct:
            print("""Failed:
                  Got      : {alg_result}
                  Expected : {expected_result}""".format(alg_result=alg_result, expected_result=expected_result))
        else:
            print("Passed")

        run_benchmark(alg, max_exponent=max_exponent, max_element=max_element, repetitions=50)


if __name__ == '__main__':
    main()

