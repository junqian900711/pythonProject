# https://www.bilibili.com/video/BV1qK411n7gQ?p=157&spm_id_from=pageDriver
class House(object):
    # 缺省参数
    def __init__(self, house_type, total_area, fru_list=None):
        if fru_list is None:  # 如果这个值是None
            fru_list = []  # 将fru_list设置为空列表
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.6
        self.fru_list = fru_list

    def add_fru(self, x):  # x = bed/
        # print('需要将加剧添加到房子里')
        if self.free_area < x.area:
            print('剩余面积不足，放不进去了')
        else:
            self.fru_list.append(x.name)
            self.free_area -= x.area

    def __str__(self):
        # print("hello") # 此处不能使用print 方法，当print打印一个对象的时候，会查找这个对象的__repr__ / __str__ 方法，获取他们的返回值
        return '户型={}，总面积={}，剩余面积={}，家具列表={}'.format(self.house_type, self.total_area, self.free_area,
                                                     self.fru_list)


class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


# 创建房间对象的是后，传入户型和总面积
house = House('一室一厅', 20)
# 把家具添加到房间里（面向对象关注点：让谁做）

sofa = Furniture('沙发', 10)
bed = Furniture('席梦思', 4)
chest = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)


# 把家具添加到房间里（面向对象关注点：让谁做）
house.add_fru(sofa)
house.add_fru(bed)  # 调用house 对象的add_fru方法，就是"."之前的对象是谁，也就意味着self 指向的是谁
house.add_fru(chest)
house.add_fru(table)


# print(house)  # <__main__.House object at 0x01F51E68>  如果要打印，要使用__str__ OR __repr__  //相当于print(house.__str__())
print(house)
