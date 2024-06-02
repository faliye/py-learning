"""decorator"""

# def record_time(func):
    
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result
    
#     return wrapper

# import time
# import random

# def record_time(func):
    
#     def wrapper(*args, **kwargs): # args 是一个元组
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__}执行时间:{end - start:.2f}秒")
#         return result

#     return wrapper

# def download(filename):
#     """下载文件"""
#     print(f'开始下载{filename}.')
#     time.sleep(random.random() * 6)
#     print(f'{filename}下载完成.')

    
# def upload(filename):
#     """上传文件"""
#     print(f'开始上传{filename}.')
#     time.sleep(random.random() * 8)
#     print(f'{filename}上传完成.')
    
# download = record_time(download)
# upload = record_time(upload)
# download('MySQL从删库到跑路.avi')
# upload('Python从入门到住院.pdf')

"""fibonacci"""

import time

"""时间装饰器"""
# def record_time(fnc):
    
#     def wrapper(*args, **kwarge):
#         start = time.time()
#         result = fnc(*args, **kwarge)
#         end = time.time()
#         print(f"{fnc.__name__} {end - start:.2f}秒")
#         return result
    
#     return wrapper

# def fn1(a):
#     if a in (0, 1):
#         return 1
#     return a * fn1(a-1) # 半扩张式的递归

# def fn2(a):
#     if a in (1, 2):
#         return 1
#     return fn2(a-1) + fn2(a-2) # 扩张式的递归 每一环都会占用栈，所以系统负担很重 非常慢

# start = time.time()
# print(fn1(50))
# end = time.time()
# print(end -  start)

# start = time.time()
# print(fn2(50))
# end = time.time()
# print(end -  start)

def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

start = time.time()
for i in range(1, 51):
    fib2(51)
end = time.time()
print(f"{end -  start:1f}") # 0.000969

"""缓存结果"""
from functools import lru_cache

@lru_cache()
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)

start = time.time()
for i in range(1, 51):
    fib1(51)
end = time.time()
print(f"{end -  start:1f}") # 0.000000


