from math import factorial

print(factorial(1) ,factorial(5))

import module as m
import module1 as m1

m.hello()
m1.hello()

from module import hello as h
from module1 import hello as h1

h1()
h()

"""
https://github.com/jackfrued/Python-for-Freshmen-2023/blob/master/%E7%AC%AC14%E8%AF%BE%EF%BC%9A%E5%87%BD%E6%95%B0%E5%92%8C%E6%A8%A1%E5%9D%97.md#%E6%A0%87%E5%87%86%E5%BA%93%E4%B8%AD%E7%9A%84%E6%A8%A1%E5%9D%97%E5%92%8C%E5%87%BD%E6%95%B0
"""

# abs(-1.3)
# bin(123)
# hex(10)
# input("input something")
# len("123")
# max,min
# oct # 8

# OpenTextModeWriting: TypeAlias = Literal["w", "wt", "tw", "a", "at", "ta", "x", "xt", "tx"]
# open(file, "w", encoding)
# OpenTextModeReading: TypeAlias = Literal["r", "rt", "tr", "U", "rU", "Ur", "rtU", "rUt", "Urt", "trU", "tUr", "Utr"]
# open(file, "r", encoding)

# pow(2, 3) 2**3 = 8

# range(start, end)

# round(num, ndigits) # ndigits

# sum(range(start, end))

# type()