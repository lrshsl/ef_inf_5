
from random import randint


N: int = 100
MAX_ELEMENT: int = 10000


def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            j = i
            while j >= gap and arr[j - gap] > arr[j]:
                arr[j - gap], arr[j] = arr[j], arr[j - gap]
                j -= gap
        gap //= 2
    return arr


if __name__ == '__main__':
    arr = [randint(0, MAX_ELEMENT) for _ in range(N)]
    print(shell_sort(arr))


