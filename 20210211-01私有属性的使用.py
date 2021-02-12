import datetime

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 1000  # 以两个下划线开始的变量是私有变量

    def test(self):
        self.__money += 10 # 在这里可以访问私有属性

    def get_money(self):
        # 记录
        print('{}查询了余额'.format(datetime.datetime.now()))
        return self.__money

    def set_money(self, qian):
        if type(qian) != float:
            print('wrong type')
            return
        print('修改余额了')
        self.__money = qian

    def __demo(self):  # 以两个下划线开始的函数，是私有函数，在外部无法调用
        print('我是demo 函数')

    def __test(self):
        self.__demo()

p1 = Person('zhangsan', 18)
p2 = Person('lisi', 19)

print(hex(id(p1)))
# print(p1.__money)#可以直接获取到name、age   但是不能直接获取私有变量

#p1.test()


# p1.__demo() #'Person' object has no attribute '__demo' 不能直接调用demo 函数，它是私有方法
# p1._Person__demo() #可以这样硬调

# 获取私有变量的方式：
# 1.通过是用对象._类名__私有变量名获取
print(p1._Person__money) # 通过这种方式也能获取到私有属性

# 2.定义get 和set 方法来获取
print(p1.get_money())

# print(p1.set_money(100))
print(p1.set_money('hello'))
print(p1.get_money())
# 3.通过property（）方法来获取
