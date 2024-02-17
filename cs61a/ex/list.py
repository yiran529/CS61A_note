total=0
s=[1,2,3,4,5]
for i in s:
    total+=1
print(total)
s=['adsfas']
s.extend('da')
print(s)
d={'x':1,'y':2,'z':3}
print(list(d.keys()))
print(sum([[1,2,3,4],[9,10]],[]))
l=[1,2,3]
l.append(4)
print(l[::-1])
print(l[3:0:-1])
def even_weighted(s):
    return [i*s[i] for i in range(len(s)) if i%2==0]
print(even_weighted([1,2,3,4,5]))
def max_product(s):
    if s==[]:return 1
    else: return max(s[0]*max_product(s[2:]),max_product(s[1:]))
print(max_product([5,10,5,10,5]))

s=[1,2,3]
t=[5,6]
s[3:]=[t]
t[1]=10
print(s)