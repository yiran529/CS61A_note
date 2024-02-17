def fib(n=10):
    pre , cur = 1 , 1
    k = 1
    while k < n:
        pre , cur = cur , pre + cur
        k = k + 1
    return cur
print(fib())