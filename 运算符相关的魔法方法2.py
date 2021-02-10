class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "正在吃东西")

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __ne__(self, other):  # 使用！= 运算符会自动调用这个方法
        return 'hello'

    def __gt__(self, other):  # greater than/ 调用'>' 会自动调用
        return self.age > other.age

    # __ge__ greater equal
    # __lt__ less than
    # __add__   +
    # __sub__   -
    # __mul__   *
    # __truediv__   /


p1 = Person('张三', 18)
p2 = Person('张三', 18)
p3 = Person('李四', 19)
print(p1 is p2)  # false

#  ////== 运算符本质其实是调用对象的 __eq__ 方法，获取__eq__ 方法的返回结果
print(p1 == p2)
# false/ 本质是调用 __ne__方法 或者 __eq__方法取反/ 优先ne 其次eq
print(p1 != p2)

print(p1 > p3)  # '>' not supported between instances of 'Person' and 'Person' /// 调用__gt__ 方法

# str()将对象转换成字符串，会自动调用__str__ 方法
# 1. str（） 2.打印对象也会调用
x = str(p1)
print(x)  # <__main__.Person object at 0x01081E68>  转换成为字符串，默认会转换成类型+ 内存地址

print(int(p1))  # 只调用了__init__,没有调用__str__
print(p1)  # 调用__str__
