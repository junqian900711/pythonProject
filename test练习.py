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
# https://blog.csdn.net/weixin_44133442/article/details/102408411
def getDict(dic2):
    return {value: key for key, value in dic2.items()}


# 编写一个函数，提取指定字符串中所有字母，然后凭借在一起产生一个新的字符串
def get_alphas(word):
    new_str = ''
    for w in word:
        if w.isalpha():
            new_str += w
    return new_str


# 写一个函数，默认求10 的阶乘，也可以求其他数字的阶乘
# 缺省函数
def get_factorial(n=10):
    x = 1
    for i in range(1, n + 1):
        x *= i
    return x


# 写一个函数，求多个数的平均值
def get_ave(*args):
    total_sum = 0
    for arg in args:
        total_sum += arg
    return total_sum / len(args)


# 写一个函数，能够将制定字符串的首字母变成大写字母
def my_capitalize(word):
    string_first = word[0]
    if 'a' <= string_first <= 'z':
        new_str = word[1:]
        return string_first.upper() + new_str
    return word


# 写一个自己的endswith 函数,判断一个字符串是否以指定的字符串结束
def endswith(old_str, str1):
    return old_str[-len(str1):] == str1


# 判断一个字符串是否是纯数字字符串
def isdigit(old_str):
    for i in old_str:
        if not '0' <= i <= '9':
            return False
    return True


# 写一个upper 函数，将一个字符串的所有小写字母变成大写字母
# a-》97   A-》65
def my_upper(old_str):
    new_string = ''
    for i in old_str:
        if 'a' <= i <= 'z':
            upper_string = chr(ord(i) - 32)
            new_string += upper_string

        else:
            new_string += i
    return new_string


# 写一个自己的replace 函数，将指定字符串中指定的旧字符串转换成指定的新字符串
def my_replace(all_str, old_str, new_str):
    # #第一种办法： 先进行切割，再进行join
    # return new_str.join(all_str.split(old_str))

    # method 2
    # https://www.bilibili.com/video/BV1qK411n7gQ?p=156&spm_id_from=pageDriver  三个三个的切，但是一个一个的加
    result = ''
    i = 0
    while i < len(all_str):
        temp = all_str[i:i + len(old_str)]
        if temp != old_str:
            result += all_str[i]
            i += 1
        else:
            result += new_str
            i += len(old_str)
    return result


# 写一个自己的max 函数，获取指定序列中元素的最大值，如果序列是字典，取字典值的最大值
def get_max2(seq):
    # if type(seq) == dict:
    # 此時的dict 拿到的是dict 的value的值，不能夠像list 那樣去切片，必须转为list
    if isinstance(seq, dict):  # 面向对象的语法，看对象seq是否是通过dict类创建出来的实例
        seq = list(seq.values())
        print(seq)

    x = seq[0]
    for i in seq:
        if i > x:
            x = i
    return x


# print(getMax(1, 9, 65, 345, 12, 6, 12, 76, 234))
# print(get_Sum(5))
#
# dict_ori = {'A': 1, 'B': 2, 'C': 3}
# print(getDict(dict_ori))
#
# print(get_alphas('hello123good456'))
#
# print(get_factorial(4))
# print(get_factorial())
#
# print(get_ave(1, 3, 5, 6, 6, 3, 7))
#
# print(my_capitalize('354hello'))
#
# print(endswith("hello", 'llo'))
#
# print(isdigit('123hfdg90'))

print(my_upper('asdAQfqSWR42354FECsda'))

print(my_replace("how you and you fine you ok", 'you', 'me'))

print(get_max2([2, 4, 6, 8, 9, 0, 3, 65]))
print(get_max2({'x': 10, 'y': 34, 'c': 2354, 'u': 15, 'k': 77, 'd': 95, 'b': 1, 'i': 10, 'a': 10}))
