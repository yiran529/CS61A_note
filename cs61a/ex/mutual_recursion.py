def split(x):#将split功能单独搞成一个函数
    return x//10,x%10
def sum_digits(x):
    if x<10:
        return x
    else:
        return sum_digits(x//10)+x%10
def luhn_sum(x):
    if x<10:# the base case!
        return x
    else:
        last_but_one,last=split(x)
        return luhn_double_sum(last_but_one)+last
def luhn_double_sum(x):
    last_but_one,last=split(x)
    luhn_digit=sum_digits(last*2)
    if x<10:
        return luhn_digit
    else:
        return luhn_sum(last_but_one)+luhn_digit
print(luhn_sum(5105105105105100))