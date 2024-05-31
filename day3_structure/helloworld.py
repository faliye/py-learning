# list type
# list = [1, 2, 3, 4]

#list(iterable) function
# list4 = list(range(4))

# list contact +
# list1 = [1]
# list2 = [2, 3]
# print(list1+list2) # [1, 2, 3]

# list repeat * num
# list1 = [1] * 3
# list2 = ["a"] * 3
# print(list1, list2)

# list[start, end, step]
# items = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
# print(items[0:5:2])     # ['apple', 'durian', 'watermelon']
# print(items[::2])     # ['apple', 'durian', 'watermelon']
# print(items[-2:-6:-1])  # ['peach', 'durian', 'strawberry', 'apple']
# print(items[3:-10:-1])  # ['peach', 'durian', 'strawberry', 'apple']
# print(items[-4:-2])   # ['strawberry', 'durian']
# print(items[-2::-1])  # ['peach', 'durian', 'strawberry', 'apple']


# list[start, end] = list
# items = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
# items[1:3] = ["0", "3"]
# print(items)  # ['peach', 'durian', 'strawberry', 'apple']
# items[1:4] = ["0", "3"]
# print(items)  # ['peach', 'durian', 'strawberry', 'apple']

# remove(ele)
# items = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
# items.remove(items[2])
# print(items)

# pop(ele)

# append(ele)

# clear() []

# index(ele, startIndex)


"""

tuple 一旦定义不可改变

"""
# a = 1, 2, 3  # 定义方式1
# print(type(a))

# a = (1, 2, 3) # 定义方式2

# print(type(a))

# # 互相转换
# list = [1, 2, 3]

# tu =  tuple(list)

# list = list(tu)