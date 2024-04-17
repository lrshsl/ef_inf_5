#include <functional>
#include <iostream>
#include <random>

// Header {{{

// %pragma once		// Add when header file

#define N 100
#define MAX_ELEMENT 10000

void shell_sort(int arr[], int n);

class ShellSort {
public:
  void sort(int arr[], int n);
};

// }}}

int main() {

  // Array with random numbers
  std::default_random_engine generator;
  std::uniform_int_distribution<int> distribution(0, MAX_ELEMENT);
  auto randint = std::bind(distribution, generator);
  int arr[N], i;
  for (i = 0; i < N; i++)
    arr[i] = randint();

  // Sort
  shell_sort(arr, N);

  // Print
  for (i = 0; i < N; i++)
    std::cout << arr[i] << " ";
}

void ShellSort::shell_sort(int arr[], int n) {
  int gap, j, temp;
  for (gap = n / 2; gap > 0; gap /= 2) {
    for (int i = gap; i < n; i++) {
      temp = arr[i];
      for (int j = i; j >= gap && arr[j - gap] > temp; j -= gap)
        arr[j] = arr[j - gap];
      arr[j] = temp;
    }
  }
}
