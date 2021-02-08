# https://blog.csdn.net/weixin_44133442/article/details/102408411（更改字典的key 和value）
import random


# 编写一个函数，求多个数中最大的值
def getMax(*args):
    x = args[0]
    for arg in args:
        if x < arg:
            x = arg
    return x


# 编写一个函数，实现摇色子的功能，打印N个筛子的点数和
def get_Sum(n):
    m = 0
    for i in range(n):
        x = random.randint(1, 6)
        print("n = {} and x = {}".format(i, x))
        m += x
    return m


# 指定更改dictionary
#https://blog.csdn.net/weixin_44133442/article/details/102408411
def getDict(dic2):
    return {value: key for key, value in dic2.items()}


#编写一个函数，提取指定字符串中所有字母，然后凭借在一起产生一个新的字符串
def get_alphas(word):
    new_str = ''
    for w in word:
        if w.isalpha():
            new_str += w
    return new_str

#写一个函数，默认求10 的阶乘，也可以求其他数字的阶乘
#缺省函数
def get_factorial(n = 10):
    x = 1
    for i in range(1,n+1):
        x *= i
    return x


print(getMax(1, 9, 65, 345, 12, 6, 12, 76, 234))
print(get_Sum(5))

dict_ori = {'A': 1, 'B': 2, 'C': 3}
print(getDict(dict_ori))

print(get_alphas('hello123good456'))

print(get_factorial(4))
print(get_factorial())