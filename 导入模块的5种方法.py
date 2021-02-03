# https://www.bilibili.com/video/BV1qK411n7gQ?p=135&spm_id_from=pageDriver


# 1.使用import 模块直接导入一个模块
import time

print(time.time())

# 2.from 模块名import 函数名，导入一个模块里的一个方法或者变量
from random import randint

print(randint(0, 3))  # [0,3] 随机数

# 3.from 模块名import* 导入这个模块里的“所有”方法和变量
from math import *

print(pi)

# 4.导入一个模块并给一个别名
import datetime as dt

print(dt.MAXYEAR)

# 5.from 模块名 import 函数名 as 别名
from copy import deepcopy as dp

dp(['hello', 'good', [1, 2, 3], 'hi'])



import os

print(os.path.abspath("名片管理系统.py"))
fil_name = '2020.2.22.demo.py'
print(os.path.splitext(fil_name))
print(fil_name.rpartition('.'))


