class Singleton(object):
    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self, a, b):
        self.a = a
        self.b = b

# 1. 调用__new__方法申请内存
s1 = Singleton('hehe', 'heiheihei')
s2 = Singleton('haha', 'xixixi')
