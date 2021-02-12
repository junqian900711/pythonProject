class Person(object):
    type = '人类'  # 这个属性定义在类里，函数之外，我们称之为类属性 /类属性保存在类对象里

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 对象p1 和p2 是通过Person 类创建出来的实例对象
# name 和age是对象属性，在__init__方法里，以参数的形式定义的
# 每一个实例对象都会单独保存一份的属性
# 每个实例对象之间的属性没有关联，互不影响
p1 = Person('zhangsan', 18)
p2 = Person('lisi', 19)

print('0x%X, ox%X' % (id(p1), id(p2)))

# 类属性可以通过类对象和实例对象获取
print(Person.type)  # 可以通过类对象获取类属性
print(p1.type)  # 可以通过实例对象获取类属性

# 类属性只能通过类对象修改，实例对象无法修改类
p1.type = 'human'
print(p1.type)  # 并不会修改类属性，而是给实例对象添加了一个新的对象属性
print(p2.type)

Person.type = 'Monkey'  # 修改了类属性
print(p2.type)
print(p1.type)
