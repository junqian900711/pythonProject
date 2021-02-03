import time


# https://www.bilibili.com/video/BV1qK411n7gQ?p=132&spm_id_from=pageDriver
def cal_time(fn):
    print("我是外部函数，我被调用了")
    print("fn={}".format(fn))

    def inner():
        start = time.time()
        # fn()
        s = fn()
        end = time.time()
        print("time is ", end - start)
        return s #针对的是return x的情况
    return inner


# 第一件事调用cal-time/第二件事把被装饰的函数传递给fn   语法糖
def demo():
    x = 0
    for i in range(1, 1000000000):
        x += 1
    #print(x)
    return x #如果是返回值

# @cal_time  # 想用就加，不想要记得删除
# def foo():
#     print("hello")
#     time.sleep(3)
#     print("world")


# demo() #第三件事;当你再次调用demo函数时，demo函数已经不再是上面的demo
#foo() #调用
# print("foo = ", foo)

m = demo()
print('m 的值是', m)  #m = none

