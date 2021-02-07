# 魔法方法，也叫魔術方法,是内里的特殊的一些方法
# 特点
# 1.不需要手动调用，会在合适的时机自动调用
# 2，这些方法，都是使用__开始，使用__结束
# 3. 方法名都是系统规定好的，在合适的时机自己调用
# https://www.bilibili.com/video/BV1qK411n7gQ?p=153&spm_id_from=pageDriver
import time
import datetime

x = datetime.datetime(2020, 2, 24, 16, 17, 45, 200)
print(x)  # __str__ method
print(repr(x))  # __repr__method


# 2020-02-24 16:17:45.000200    __str__更在乎可读性
# datetime.datetime(2020, 2, 24, 16, 17, 45, 200)  __repr 更在乎准确性


class Person(object):

    def __init__(self, name, age):
        # 在创建对象时，会自动调用这个方法
        print('__init__被调用了')
        self.name = name
        self.age = age

    def __del__(self):
        # 当对象被销毁时，会自动调用这个方法
        print('__del__被调用了')

    def __repr__(self):
        return 'hello'

    def __str__(self):
        return '姓名：{}， 年龄：{}'.format(self.name, self.age)

    def __call__(self, *args, **kwargs):
        print('__call__ call 方法被调用了')
        # args 是一个元祖，保存（1,2）
        # kwargs 是一个字典 {fn：lamda x,y :x +y}
        print('args = {}, kwargs= {}'.format(args, kwargs))
        # args = (1, 2), kwargs= {'fn': <function <lambda> at 0x00E48778>}
        test = kwargs['fn']
        return test(args[0], args[1])  # 注意return 的书写


p = Person('zhangsan', 18)
# print(p) #如果不做任何的修改，直接打印一个对象，是文件的__name__.型以 内存地址
# <__main__.Person object at 0x00F1B028>


# 当打印一个对象的时候，会调用对象的 __str__ 或者 __repr__ 方法
# 如果两个方法都谢了，会选择__str__
print(p)

# print(repr(p))  # 调用内置函数repr 会出发对象的__repr__方法
# print(p.__repr__())  # 魔法方法，一般不手动调用

# del p
# time.sleep(10)


# p(1, 2)  # 对象名（） --》 调用这个对象的__call__方法
n = p(1, 2, fn=lambda x, y: x + y)
print(n)
