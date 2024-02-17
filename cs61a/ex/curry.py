from operator import add
exec('curry=lambda f: lambda x :lambda y: f(x,y)')
#curry的参数是f，返回值是lambda函数，该lambda函数的参数是x，返回值是一个lambda函数
#该函数参数是y，返回值是f(x,y)
print(curry(add)(3)(4))
""""ssa
sdf
dsaf"""
"fasd"