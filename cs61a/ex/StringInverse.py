def inverse(s):
    if len(s)==1:
        return s
    else:
        return  inverse(s[1:])+s[0]
print(inverse("hello"))



print(bool(""))