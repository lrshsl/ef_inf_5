#include <stdio.h>
#include <stdlib.h>

// Header {{{
#ifndef SHELL_SORT_H
#define SHELL_SORT_H

#define N 100
#define MAX_ELEMENT 10000

void shell_sort(int a[], int n);
static inline void swap(int *a, int *b);
inline void sort_with_gap(int a[], int n, int i, int gap);

#endif /* SHELL_SORT_H */

// }}}

int main() {
  int a[N];
  int i = 0;
  for (i = 0; i < N; i++)
    a[i] = rand() % MAX_ELEMENT;

  shell_sort(a, N);

  for (i = 0; i < N; i++)
    printf("%d ", a[i]);
  printf("\n");
  system("pause");
  return 0;
}

void shell_sort(int array[], int len) {
  int gap, i;
  for (gap = len / 2; gap > 0;
       gap /= 2) {                // Make gap smaller (n/2, n/4, n/8, ...)
    for (i = gap; i < len; i++) { // Go through array with index `i`
      sort_with_gap(array, len, i, gap);
    }
  }
}

inline void sort_with_gap(int array[], int len, int i,
                          int gap) { // Insertion sort
  int temp = array[i];
  for (; i >= gap && array[i - gap] > temp; i -= gap)
    array[i] = array[i - gap];
  array[i] = temp;
}

static inline void swap(int *a, int *b) {
  *a ^= *b;
  *b ^= *a;
  *a ^= *b;
}
