

def shell_sort(arr, n):

    gap = n // 2

    while gap >= 1:

        # Gehe mit dem 'Fenster' der grösse `gap` bis zum letzten Element
        for i in range(0, n - gap, gap):

            # Gehe durch alle Elemente mit dem entsprechenden Abstand

            # Hier wird Insertion Sort verwendet
            while i >= 0 and arr[i + gap] < arr[i]:
                arr[i + gap], arr[i] = arr[i], arr[i + gap]
                i -= 1

        gap //= 2

    return arr


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
n = len(arr)

print(shell_sort(arr, n))
