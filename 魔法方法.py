#魔法方法，也叫魔術方法,是内里的特殊的一些方法
#特点
#1.不需要手动调用，会在合适的时机自动调用
#2，这些方法，都是使用__开始，使用__结束
#3. 方法名都是系统规定好的，在合适的时机自己调用
#https://www.bilibili.com/video/BV1qK411n7gQ?p=153&spm_id_from=pageDriver


class Person(object):

    def __init__(self,name,age):
        #在创建对象时，会自动调用这个方法
        print('__init__被调用了')
        self.name = name
        self.age = age

    def __del__(self):
        print('__del__被调用了')


p=Person('zhangsan',18)