def search(f):
    x=0
    while not f(x):
        x+=1
    return x
def inverse(f):
    return lambda y:search(lambda x:f(x)==y)
def square(x):
    return x*x
sqrt=inverse(square)
print(sqrt(100))