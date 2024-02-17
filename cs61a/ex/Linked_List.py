class Link:
    empty=()
    def __init__(self,first,rest=empty):
        self.first=first
        self.rest=rest
    def __str__(self):
        s='< '
        link=self
        while link:
            s=s+str(link.first)+' '
            link=link.rest
        s+='>'
        return s
def Link_range(start,end):
    if start<end:
        return Link(start,Link_range(start+1,end))
    else:return Link.empty
def Link_map(f,link):
    if link:
        return Link(f(link.first),Link_map(f,link.rest))
    else:return Link.empty
def Link_filter(f,link):
    if link and f(link.first):
        return Link(link.first,Link_filter(f,link.rest))
    elif link and not f(link.first):
        return Link_filter(f,link.rest)
    else:return Link.empty
def add(s,v):
    assert s
    if v<s.first:
        s.first,s.rest=v,Link(s.first,s.rest)
    elif v>s.first and not s.rest:
        s.rest=Link(v)
    else: add(s.rest,v)
    return s
def square(x):
    return x*x
def odd(x):
    if x%2==1:return True
    else:return False
s=Link_range(1,6)
print(s)
t=Link_filter(odd,s)
print(Link_map(square,t))
add_t=add(t,4)
print(add_t)
