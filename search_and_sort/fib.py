def fib1(n: int) -> int:
    if n <= 1: return n;
    return fib(n - 1) + fib(n - 2);


for i in range(20):
    print(fib2(i));
