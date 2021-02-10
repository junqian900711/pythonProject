class Person(object):
    """
    这是一个人类

    """

    #__slots__ = ('name','age')  #规定了对象可以出现的属性就是name 和 age

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃饭')


p1 = Person('张三', 18)
print(dir(p1))
print(p1.__class__)  # <class '__main__.Person'>
print(p1.__dict__)  # 把对象属性和值转换成一个字典


print(p1.__doc__)  # 对象名.__doc__
print(Person.__doc__)  # 类名.__doc__

print(p1.__module__)  #__main__