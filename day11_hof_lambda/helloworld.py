"""
calc
"""
# def calc(*arg, **kwargs):
#     print(arg, kwargs)
#     items = list(arg)+list(kwargs.values())
#     result = 0
#     for val in items:
#         if type(val) in (int, float):
#             result += val
#     return result


# def calc(init_value, fnc, *arg, **kwargs):
#     items = list(arg)+list(kwargs.values())
#     result =  init_value
#     for val in items:
#         if(type(val) in (int, float)):
#             result = fnc(result, val)
        
#     return result


# old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']

# print(sorted(old_strings))

# old_nums = [35, 12, 8, 99, 60, 52]

# print( [i *2 for i in old_nums if i%2 ==0])


# old_nums = [35, 12, -8, 99, 60, 52]

# print(list(filter(lambda x: True if x>0 else False, old_nums)))

"""
https://github.com/jackfrued/Python-for-Freshmen-2023/blob/master/
%E7%AC%AC16%E8%AF%BE%EF%BC%9A%E5%87%BD%E6%95%B0%E4%BD%BF%E7%94%A8%E8%BF%9B%E9%98%B6.md
"""

# import operator
# import functools

# fac = lambda x: functools.reduce(operator.mul,range(2, x+1), 1)

# print(fac(3))


# 用一行代码实现判断素数的函数
# all 如果全是true则返回true
# any 如果有一个true为true
# is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))


"""
*args
**kwargs
"""
# def foo(*args, **kwargs):
#     print(args) # (3, 2.1, True)
#     print(kwargs) #  {'name': '骆昊', 'age': 43, 'gpa': 4.95}

# foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)

import random
import string

ALL_CHAR = string.digits + string.ascii_letters

def generate_code(*,code_len= 6):
    return "".join(random.choices(ALL_CHAR, k= code_len))

print(generate_code())