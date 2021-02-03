# 产品经理：提需求/改需求

#https://www.bilibili.com/video/BV1qK411n7gQ?p=133&spm_id_from=pageDriver
def cam_play(fn):
    def inner(x, y, *args, **kwargs):
        # print(args)
        # if args[0] <= 22:
        print(kwargs)
        # clock = kwargs['clock'] #有一个小问题，如果没有字典的key，就是会报错，所以用下行修改的获取方式
        clock = kwargs.get('clock',23) # 23为默认值
        if clock <= 22:
            fn(x, y)
        else:
            print('too late')

    return inner


@cam_play
# 开放封闭原则
def play_game(name, game):
    print('{} 正在玩 {}'.format(name,game))


# play_game('zhangsan', 'LOL', 18)
# play_game('lisi', 'judiqiusheng', 34)

play_game('wangwu', 'LOL', clock = 18)
play_game('maliu', 'judiqiusheng', clock= 34)
