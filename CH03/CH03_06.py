# 单向链表的连接功能
"""
设计程序建立5个学生的单向链表，然后遍历每一个节点并打印学生姓名与成绩
"""

import sys

class student:
    def __init__(self):
        self.num = 0
        self.name = ''
        self.score = 0
        self.next = None

def main():
    print('请输入5项学生数据: ')
    node  = student()
    if not node:
        print('Error!内存分配失败!!')
        sys.exit(0)
    node.num = eval(input('请输入学号: '))
    node.name = input('请输入姓名: ')
    node.score = eval(input('请输入成绩: '))
    # 保留链表头部，以ptr为当前节点指针
    ptr = node

    for i in range(1,5):
        newnode = student()
        if not node:
            print('Error!内存分配失败!!')
            sys.exit(0)
        newnode.num = eval(input('请输入学号: '))
        newnode.name = input('请输入姓名: ')
        newnode.score = eval(input('请输入成绩: '))
        newnode.next = None
        # 把新节点加在链表后面
        ptr.next = newnode
        # 让ptr保留在链表最后面
        ptr = ptr.next

    print(' 学 生 成 绩')
    print(' 学号\t姓名\t成绩\n'+'='*20)
    # 让ptr回到链表头部
    ptr = node
    while ptr != None:
        print('%3d\t%-s\t%3d'%(ptr.num,ptr.name,ptr.score))
        node = ptr
        # 按序往后遍历链表
        ptr = ptr.next

main()