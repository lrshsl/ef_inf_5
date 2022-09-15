import timeit
import matplotlib.pyplot as plt

ARRAY_LENGTH: int = 1000
NB_TEST_CASES: int = 1

def fn_insert(array_length: int):
    arr = list()
    for _ in range(array_length):
        arr.insert(0, 0)
    return arr

def fn_reverse(array_length: int):
    arr = list()
    for _ in range(array_length):
        arr.append(0)
    arr.reverse()
    return arr

def fn_reversed(array_length: int):
    arr = list()
    for _ in range(array_length):
        arr.append(0)
    return reversed(arr)

def fn_own_iterator(array_length: int):
    for _ in range(array_length):
        yield 0


def mesure_insert(): fn_insert(ARRAY_LENGTH)
def mesure_reverse(): fn_reverse(ARRAY_LENGTH)
def mesure_reversed(): fn_reversed(ARRAY_LENGTH)
def mesure_own(): fn_own_iterator(ARRAY_LENGTH)

def test_fn(fn):
    expected_values = (0 for _ in range(ARRAY_LENGTH))
    for i, x in enumerate(fn()):
        assert x == expected_values[i]

times_insert_method = list()
times_reverse_method = list()
times_reversed_method = list()
times_own = list()

for _ in range(NB_TEST_CASES):
    times_insert_method.append(
        timeit.Timer(mesure_insert).timeit())
    times_reverse_method.append(
        timeit.Timer(mesure_reverse).timeit())
    times_reversed_method.append(
        timeit.Timer(mesure_reversed).timeit())
    times_own.append(
        timeit.Timer(mesure_own).timeit())

plt.plot(
    times_insert_method, "",
    times_reverse_method, "",
    times_reversed_method, "",
    times_own, "",
)
plt.show()
