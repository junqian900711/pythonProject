class Person(object):

    def __init__(self, name, age):
        # 在创建对象时，会自动调用这个方法
        # print('__init__被调用了')
        self.name = name
        self.age = age

    def __eq__(self, other):
        print('__eq__ 方法被调用了, others= ', other)
        # if self.name == other.name and self.age == other.age:
        #     return True
        #
        # return False
        return self.name == other.name and self.age == other.age


# 1.调用__new__ 方法申请内存空间
p1 = Person('zhangsan', 18)
p2 = Person('zhangsan', 18)

print('0x%X' % id(p1))
print('0x%X' % id(p2))
print(p1 is p2)
# _-eq__如果不重写，默认比较依然是内存地址/ 请参考重写___eq__方法,获取这个方法的返回值
print(p1 == p2)  # p1 == p2 本质是调用p1.__eq__(p2)
# False
# False

nums1 = [1, 2, 3]
nums2 = [1, 2, 3]

print(nums1 is nums2)
print(nums1 == nums2)
# False
# True

# is 比较两个对象的内存地址
# ==会调用对象的__eq__ 方法，获取这个方法的比较结果
