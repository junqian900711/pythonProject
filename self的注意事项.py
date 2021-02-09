class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "正在吃东西")
