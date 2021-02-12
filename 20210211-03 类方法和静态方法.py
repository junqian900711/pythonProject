# https://www.bilibili.com/video/BV1qK411n7gQ?p=165&spm_id_from=pageDriver  (图解)

class Calculator(object):
    @staticmethod
    def addall(a, b):
        return a + b


c = Calculator()
c.addall(1, 2)

print(Calculator.addall(1, 2))


class Person(object):
    type = 'human'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):  # 对象方法有一个参数self，指的是实例对象
        print(self.name + ' eating ' + food)

    # 如果一个方法里没有用到实例对象的任何属性，可以将这个方法成static
    @staticmethod
    def demo():
        # def demo(self):  # 默认的方法都是对象方法
        print("hello")

    @classmethod
    def test(cls):  # 如果这个函数值用到了类属性，我们可以把它定义为一个类方法
        # 类方法会有一个参数cls，也不需要手动传参， 会自动传参
        # cls 指的是对象  cls is Person
        print(cls.type)
        print('yes')


p = Person('zhangsan', 18)
p2 = Person('李四', 20)

# 实例对象在调用方法的时候，不需要给形参self 传参，会自动的把实例对象传递给self
# eat 对象方法，可以直接使用实例对象，方法名（参数）调用
# 使用对象名.方法名(参数)调用的方式，不需要传递self
# 会自动将对象名传递给self
p.eat('sushi')  # 直接使用实例对象调用方法

# 对象方法还可以是用类对象来调用类名.方法名（）
# 这种方式，不会自动给self 传参，需要手动的指定self
print(Person.eat(p2, 'rice'))

# print(p.eat)
# print(p2.eat)
# print(p.eat is p2.eat)
# print(Person.eat)
# <bound method Person.eat of <__main__.Person object at 0x02FD1E68>>
# <bound method Person.eat of <__main__.Person object at 0x02FEB1A8>>
# False      / 绑定方法。。。其实不是一类的
# <function Person.eat at 0x02CD8388>


# 静态方法: 没有用到实例对象的任何属性
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
Person.demo()
p.demo()

# 类方法： 可以使用实例对象和类对象调用
p.test()
Person.test()
