import time

def cal_time(fn):
    print("我是外部函数，我被调用了")
    print("fn={}".format(fn))



    def inner():
        start = time.time()
        fn()
        end = time.time()
        print("time is ", end-start)
    return inner

@cal_time   #第一件事调用cal-time/第二件事把被装饰的函数传递给fn   语法糖
def demo():
    x = 0
    for i in range(1, 1000000000):
        x += 1
    print(x)


demo() #第三件事;当你再次调用demo函数时，demo函数已经不再是上面的demo
