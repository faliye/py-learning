"""
My first python program.(lie)
Start with Hello world.
 
version: 0.0.1
"""
print("hello world")

# int(string|number, pax)
print(int("12", base=16))
print(int("1", base=2))
print(int(True))

# bool(s)
print(bool("a"))
# chr(int)
print(chr(65))
# ord(str)
print(ord("A")) 
print(ord('A'))

'''
operator

'''
'''
// 整除
 
'''

print(2//3)

# [:]
# b = a[i:j]   # 表示复制a[i]到a[j-1]，以生成新的list对象
a = [0,1,2,3,4,5,6,7,8,9]
b = a[1:3]   # [1,2]

a='python'
b=a[::-1]
print(b) #nohtyp
c=a[::-2]
print(c) #nhy
#从后往前数的话，最后一个位置为-1
d=a[:-1]  #从位置0到位置-1之前的数
print(d)  #pytho
e=a[:-2]  #从位置0到位置-2之前的数
print(e)  #pyth

'''

b = a[i:j]   # 表示复制a[i]到a[j-1]，以生成新的list对象

# 当i缺省时，默认为0，即 a[:3]相当于 a[0:3]
# 当j缺省时，默认为len(alist), 即a[1:]相当于a[1:10]
# 当i,j都缺省时，a[:]就相当于完整复制一份a

b = a[i:j:s]    # 表示：i,j与上面的一样，但s表示步进，缺省为1.
# 所以a[i:j:1]相当于a[i:j]

# 当s<0时，i缺省时，默认为-1. j缺省时，默认为-len(a)-1
# 所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍，即倒序。

'''
a = [0,1,2,3,4,5,6,7,8,9]
b = a[1:3]   # [1,2]
print(b)
b = a[1:3:2] # [1]
print(b)
b = a[1:5:2] # [1, 3]
print(b)
b = a[::-1] # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(b)
b = a[-4::-1] # [6, 5, 4, 3, 2, 1, 0]
print(b)
b = a[-4:-11:-1] # [6, 5, 4, 3, 2, 1, 0]
print(b)
b = a[-4:-10:-1] # [6, 5, 4, 3, 2, 1]
print(b)
b = a[-4:-1:-1] # []
print(b)



