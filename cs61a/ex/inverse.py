def square(x):
    return x*x
def search(f):
    x=0
    while not f(x):
        x+=1
    return x
def inverse(f):
    def inverse_of_f(y):
        def is_f(x):
            return f(x)==y
        return search(is_f)
    return inverse_of_f
sqrt=inverse(square)
print(sqrt(16))
print(square(19))