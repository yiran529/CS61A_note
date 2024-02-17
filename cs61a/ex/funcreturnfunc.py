def make_adder(n):
    def adder(k):
        return n+k
    return adder
print(make_adder(1)(2))