# 多项式链表表示法
"""
设计程序，求出A=3X^3+4X+2和B=6X^3+8X^2+6X+9两个多项式相加的结果
"""

import sys

class LinkedList:
    def __init__(self):
        self.coef = 0
        self.exp = 0
        self.next = None

# 建立多项式子程序
def create_link(data):
    for i in range(4):
        newnode = LinkedList()
        if not newnode:
            print('Error!内存分配失败!!')
            sys.exit(0)
        if i==0:
            newnode.coef = data[i]
            newnode.exp = 3-i
            newnode.next = None
            head = newnode
            ptr = head
        elif data[i]!=0:
            newnode.coef = data[i]
            newnode.exp = 3 - i
            newnode.next = None
            ptr.next = newnode
            ptr = newnode
    return head

# 打印多项式子程序
def print_link(head):
    while head != None:
        if head.exp==1 and head.coef!=0:
            print("%dX+"%(head.coef),end='')
        elif head.exp!=0 and head.coef!=0:
            print("%dX^%d+"%(head.coef,head.exp),end='')
        elif head.coef!=0:
            print("%d"%head.coef)
        head = head.next
    print()

# 多项式相加子程序
def sum_link(a,b):
    i = 0
    ptr = b
    plus = [None]*4
    while a!=None:
        if a.exp == b.exp:
            plus[i] = a.coef+b.coef
            a = a.next
            b = b.next
            i += 1
        elif b.exp>a.exp:
            plus[i] = b.coef
            b = b.next
            i += 1
        elif a.exp>b.exp:
            plus[i] = a.coef
            a = a.next
            i += 1
    return create_link(plus)

def main():
    # 多项式A系数
    data1 = [3,0,4,2]
    # 多项式B系数
    data2 = [6,8,6,9]

    print('原始多项式: \nA=',end = '')
    a = create_link(data1)
    print_link(a)
    print('B=',end='')
    b = create_link(data2)
    print_link(b)
    print('多项式相加结果: \nC=',end='')
    print_link(sum_link(a,b))

main()