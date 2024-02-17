def merge(a,b):
    x=next(a)
    y=next(b)
    while True:
        if x<y:
            yield x
            x=next(a)
        elif x>y:
            yield y
            y=next(b)
        else:x=next(a)
def sequence(start, step):
    while True:
        yield start
        start += step
a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
print([next(result) for _ in range(100)])
