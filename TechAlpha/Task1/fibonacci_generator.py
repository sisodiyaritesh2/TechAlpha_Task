def fibonacci_generator():
    a,b=0,1
    while True:
        yield a
        a,b = b,a+b

n = int(input("Enter the number to print fibonacci: "))
fib = fibonacci_generator()
for _ in range(n):
    print(next(fib),end=' ')
