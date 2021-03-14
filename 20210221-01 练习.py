class Person(object):
    __count = 0 # 私有的类属性

    def __new__(cls, *args, **kwargs):
        # pass
        cls.__count += 1
        x = object.__new__(cls)  # 申请内存，创建一个对象，并设置类型是Person类
        return x

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_count(cls): #cls 指的是类对象
        return cls.__count



# 每次创建对象， 都会调用 __new__ 和 __init__ 方法
# 调用__new__方法，用来申请内存
# 如果不重写__new__方法，它会自动找object 的 __new__
# object 的__new__方法, 默认实现是申请了一段内存，创建一个对象

p1 = Person('张三', 18)
p2 = Person('李四', 18)
p3 = Person('jack', 20)
print(p1, p2, p3)

Person.__count = 100

print(Person.get_count())
# print(Person.__count)

# 申请了内存，创建了一个对象， 被设置它的类型是person
p4 = object.__new__(Person)
p4.__init__('tony', 13)
