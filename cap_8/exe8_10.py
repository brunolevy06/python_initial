def fibonacci(n):
    fibo = 1
    while n > 1:
        fibo *= n
        n-=1
    return fibo

for x in range(7):
    print("fibonacci(%d) = %d" % (x,fibonacci(x)))
