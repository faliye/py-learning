"""
set
"""
# set
# set = {1, 2, 3, 4, 5}
# set = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}

# in
# not in

# & 交集
# intersection 交集
# set1 = {1, 2, 3, 4, 5, 6, 7, 8}
# set2 = {2, 4, 6, 8}
# print(set1 & set2)
# print(set1.intersection(set2))

# | 并集
# union() 并集
# set1 = {1, 2, 3, 4, 5, 6, 7, 8}
# set2 = {2, 4, 6, 8}
# print(set1 | set2)
# print(set1.union(set2))

# - 差集
# difference()
# set1 = {1, 2, 3, 4, 5, 6, 7, 8}
# set2 = {2, 4, 6, 8}
# print(set1 - set2)
# print(set1.difference(set2))
# print(set2 - set1)
# print(set2.difference(set1))

# ^ 对称差
# symmetic_difference() 对称差
# set1 = {1, 2, 3, 4, 5, 6, 7}
# set2 = {2, 4, 6, 8}
# print(set1 ^ set2) # {1, 3, 5, 7, 8}
# print(set1.symmetric_difference(set2)) # {1, 3, 5, 7, 8}

# update 
# set1 = {1, 2, 3, 4, 5, 6, 7}
# set2 = {2, 4, 6, 8}
# set1.update(set2) # {1, 2, 3, 4, 5, 6, 7, 8}

# <= 子集
# issubset 子集
# issuperset 超集
# set1 = {2, 4, 6, 8}
# set2 = {2, 4, 6, 8}
# print(set1 <= set2)

# add()
# remove()
# discard()
# clear()
# set1 = {2, 4, 6, 8}
# set1.clear()
# print(set1)

# isdisjoint() 是否有不同元素
# set1 = {2, 4, 6, 8}
# set2 = {2, 4, 6, 8}
# print(set1.isdisjoint(set2))

# frozenset()

"""
dist
"""
# person = {}

# for _ in person:

# in

# keys()

# values()

# items()

# get()

# update()
# person1 = {'name': '王大锤', 'age': 55, 'height': 178}
# person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
# person1.update(person2)
# print(person1)  # {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}

# pop()
# popitem()
# clear()