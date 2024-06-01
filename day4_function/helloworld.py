# https://github.com/jackfrued/Python-for-Freshmen-2023/blob/master/%E7%AC%AC15%E8%AF%BE%EF%BC%9A%E5%87%BD%E6%95%B0%E7%9A%84%E5%BA%94%E7%94%A8.md

# function 
# def functionName (params):
    # functionBody
  
"""generate_code 生成指定长度的随机字符"""  
# import random
# import string

# ALL_CHARS = string.digits + string.ascii_letters

# def generate_code(*, code_len):
#     return ''.join(random.choices(ALL_CHARS,k=code_len))

# while 1:
#     print(generate_code(code_len=20))
#     str = input("continue?")
#     if(str != 'y'):
#         break
 
 
"""is_prime 测试素数"""  
# def is_prime(num: int) -> bool:
#     for i in range(2, int(num ** 0.5)+1):
#         if(num % i == 0):
#             return False
#     return True

"""欧几里得算法"""

# def gcd(x: int, y: int) -> int:
#     while y % x != 0:
#         x, y = y % x, x
#     return x

"""极差"""

# def ptp(data):
#     return max(data) - min(data)

"""算数平均"""

# def mean(data):
#     return  sum(data) / len(data)

"""中位数"""

# def median(data):
#     temp, size = sorted(data), len(data)
#     if(size % 2 != 0):
#         return temp[size//2]
#     else:
#         return median(temp[size//2 -1, size // 2 + 1]) # 这一点处理的很棒

"""方差"""
    
# def var(data, ddof=1):
#     x_bar = mean(data)
#     temp = [(num - x_bar) ** 2 for num in data]
#     return sum(temp) / (len(temp) - ddof)

"""标准差"""

# def std(data, ddof=1):
#     return var(data, ddof) ** 0.5

"""变异系数"""

# def cv(data, ddof=1):
#     return std(data, ddof) / mean(data)

