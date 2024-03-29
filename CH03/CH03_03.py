# 在单项链表中删除节点
"""
设计程序，可以在链表中删除节点。在最后离开时，列出此链表最后所有节点数据
"""

import sys

class employee:
    def __init__(self):
        self.num = 0
        self.salary = 0
        self.name = ''
        self.next = None

# 删除节点子程序
def del_ptr(head,ptr):
    top = head
    # 情形1:要删除的节点在链表头部
    if ptr.num == head.num:
        head = head.next
        print('已删除第%d号员工 姓名:%s  薪资:%d'%(ptr.num,ptr.name,ptr.salary))

    else:
        # 找到删除节点的前一个位置
        while top.next != ptr:
            top = top.next
        # 情形2:要删除的节点在链表末尾
        if ptr.next == None:
            top.next = None
            print('已删除第%d号员工 姓名:%s  薪资:%d'%(ptr.num,ptr.name,ptr.salary))
        # 情形3:删除在链表中的任一节点
        else:
            top.next = ptr.next
            print('已删除第%d号员工 姓名:%s  薪资:%d'%(ptr.num,ptr.name,ptr.salary))
    return head

def main():
    findword = 0
    namedata = ['Allen','Scott','Marry','John','Mark','Ricky','Lisa','Jasica','Hanson','Amy','Bob','Jack']
    data = [[1001,32367],[1002,24388],[1003,27556],[1007,31299],
            [1012,42660],[1014,25676],[1018,44145],[1043,52182],
            [1031,32769],[1037,21100],[1041,32196],[1046,25776]]
    print('员工编号 薪水 员工编号 薪水 员工编号 薪水 员工编号 薪水')
    print('-' * 55)
    for i in range(3):
        for j in range(4):
            print('[%4d] $%5d ' % (data[j * 3 + i][0], data[j * 3 + i][1]), end='')
        print()
    print('-' * 55)

    # 建立链表头部
    head = employee()
    head.next = None

    if not head:
        print('Error!内存分配失败!!')
        sys.exit(1)
    head.num = data[0][0]
    head.name = namedata[0]
    head.salary = data[0][1]
    head.next = None
    ptr = head

    for i in range(1, 12):
        newnode = employee()
        newnode.next = None
        newnode.num = data[i][0]
        newnode.name = namedata[i]
        newnode.salary = data[i][1]
        # 新建节点的next设置为None
        newnode.next = None
        # 旧节点的next设置为新节点
        ptr.next = newnode
        # 存储指针指向新节点
        ptr = ptr.next

    while(True):
        findword = int(input('请输入要删除的员工编号，要结束删除的过程，请输入-1: '))
        if findword==-1:
            break
        else:
            ptr = head
            find = 0
            while ptr != None:
                if ptr.num == findword:
                    ptr = del_ptr(head,ptr)
                    find += 1
                    head = ptr
                ptr = ptr.next
            if find == 0:
                print('######没有找到######')


        ptr = head
        print('\t员工编号   姓名\t薪水')
        print('\t'+'='*30)
        while ptr != None:
            print('\t[%2d]\t[ %-10s]\t[%3d]'%(ptr.num,ptr.name,ptr.salary))
            ptr = ptr.next

main()