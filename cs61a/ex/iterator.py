s=[2,3,4]
t=iter(s)
print(t)
f=lambda y: y>=10
it=iter([1,10,124])
fil=filter(f,[1,10,23])
print(next(fil))
print(next(fil))
m=map(lambda x:x*2,[2,2,4])
print(next(m))