def men():
    print("\t*****************")
    print("\t  名片管理系统\n")
    print("\t  1.添加名片\n")
    print("\t  2.删除名片\n")
    print("\t  3.修改名片\n")
    print("\t  4.查询名片\n")
    print("\t  5.退出系统\n")
    print("\t 0.显示所有名片\n")
    print("\t*****************")


def increMem(aList):
    tempList = []
    tempName = input("输入新建名片名字：")
    tempList.append(tempName)
    while True:
        tempPhone = input("输入新建联系人手机号：")
        if tempPhone.isnumeric():
            break
        else:
            print("输入有误，重新输入")
    tempList.append(tempPhone)
    tempAddr = input("输入新建联系人地址：")
    tempList.append(tempAddr)
    print("输入新建联系人信息：")
    showList(tempList)
    aList.append(tempList)


def showList(aList):
    print("名字: %s" % aList[0],
          "电话：%s" % aList[1],
          "地址：%s" % aList[2], "\n")


def showMem(aList):
    if len(aList) == 0:
        print("没有联系人!")
    for mumList in aList:
        print("名字: %s" % mumList[0],
              "电话：%s" % mumList[1],
              "地址：%s" % mumList[2], "\n")


def delMem(aList):
    i = 0
    if len(aList) == 0:
        print("没有联系人，请先添加联系人！")
        return
    tempName = input("输入要删除的联系人：")
    for mumList in aList:
        if tempName != mumList[0]:
            i += 1
            continue
        else:
            showList(aList[i])
            while True:
                tempIn = input("是否删除此联系人： Y(是)\t N(否) :")
                if tempIn == "Y" or tempIn == "y":
                    del (aList[i])
                    print("删除成功！")
                    return
                elif tempIn == "N" or tempIn == "n":
                    print("重新输入联系人！")
                    delMem(aList)
                    return
                else:
                    print("输入有误，重新输入!")
    if i == len(aList):
        print("输入的联系热不存在，请重新输入！")
        delMem(aList)


def modMem(aList):
    i = 0
    if len(aList) == 0:
        print("没有联系人，请先添加联系人！")
        return
    tempList = input("输入需要修改的联系人：")
    for numList in aList:
        if tempList != numList[0]:
            i += 1
            continue
        else:
            tempInf = input("输入修改的信息：")
            if tempInf.isnumeric():
                numList[1] = tempInf
            else:
                numList[2] = tempInf
    if i == len(aList):
        print("输入有误，重新输入！")
        modMem(aList)


def LocaMem(aList):
    i = 0
    if len(aList) == 0:
        print("没有联系人，请先添加联系人！")
        return
    tempList = input("输入需要查找的联系人：")
    for numList in aList:
        if tempList != numList[0]:
            i += 1
            continue
        else:
            showList(numList)
    if i == len(aList):
        print("输入有误，重新输入！")
        modMem(aList)


if __name__ == "__main__":
    mainList = []
    men()
    while True:
        index = input("输入任务编号：")
        if not index.isnumeric():
            print("请输入索引编号（1-4）：")
            continue
        index = int(index)
        # 遍历名片
        if index == 0:
            showMem(mainList)
        # 增加名片
        if index == 1:
            increMem(mainList)
        if index == 2:
            delMem(mainList)
        if index == 3:
            modMem(mainList)
        if index == 4:
            LocaMem(mainList)
        if index == 5:
            print("退出系统！")
            break
