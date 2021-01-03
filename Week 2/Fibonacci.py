def fib(n):
    fibonacci = [0, 1]
    for i in range(n - 1):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[n]

def test():
    print(fib(0) == 0)
    print(fib(1) == 1)
    print(fib(2) == 1)
    print(fib(3) == 2)
    print(fib(4) == 3)
    print(fib(5) == 5)
test()
