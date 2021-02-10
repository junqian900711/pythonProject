class Person(object):

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __setitem__(self, key, value):
        # print('setitem 被调用了， key={}, value= {}'.format(key,value))
        # self.key = value #尽量不要写死
        p1.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

p1 = Person('张三', 18, '襄阳')
print(p1.__dict__)  # 将对象改成字典

# 不能直接把对象当成字典来使用
p1['name'] = 'jack'  # [] 语法会调用对象的 __setitem__ 方法
p1['age'] = 20
print(p1.name, p1.age)

print(p1['name']) #此处通过getter 进行获取

