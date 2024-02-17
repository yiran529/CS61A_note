def identity(k):
    return k
def cube(k):
    return pow(k, 3)
def sumation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total
def sum(n):
    return sumation(n,cube)
print(sum(10))  
