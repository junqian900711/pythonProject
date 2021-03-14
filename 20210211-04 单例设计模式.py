# https://www.bilibili.com/video/BV1qK411n7gQ?p=166
class Singleton(object):
    __instance = None  # 类属性
    __is_first = True

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:

            cls.__instance  = object.__new__(cls) # 申请内存，创建一个对象，并把对象的类型设置为cls
        return cls.__instance

    def __init__(self, a, b):
        if self.__is_first:

            self.a = a
            self.b = b
            self.__is_first = False
# 1. 调用__new__方法申请内存
# 2. 如果不重写__new__方法，会调用object的 __new__方法
# 3. object 的__new__ 方法会申请内存
# 4. 如果重写了__new__方法，需要自己手动的申请内存
s1 = Singleton('hehe', 'heiheihei')
s2 = Singleton('haha', 'xixixi')

print(type(s1))
print(s1 is s2)