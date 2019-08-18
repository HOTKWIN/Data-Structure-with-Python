# 单向链表的反转
"""
设计程序将员工数据的链表节点按照员工号反转打印
"""

class employee:
    def __init__(self):
        self.num = 0
        self.salary = 0
        self.name = ''
        self.next = None

def main():
    findword = 0
    namedata = ['Allen', 'Scott', 'Marry', 'John', 'Mark', 'Ricky', 'Lisa', 'Jasica', 'Hanson', 'Amy', 'Bob', 'Jack']
    data = [[1001, 32367], [1002, 24388], [1003, 27556], [1007, 31299],
            [1012, 42660], [1014, 25676], [1018, 44145], [1043, 52182],
            [1031, 32769], [1037, 21100], [1041, 32196], [1046, 25776]]

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

    # 建立链表
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

    ptr = head
    i = 0
    print('反转前的员工链表节点数据:')
    # 打印链表数据
    while ptr != None:
        print('[%2d %6s %3d] => '%(ptr.num,ptr.name,ptr.salary),end = '')
        i += 1
        # 三个元素一行
        if i>=3:
            print()
            i = 0
        ptr = ptr.next

    ptr = head
    before = None
    print('\n反转后的链表节点数据:')
    # 链表反转，利用3个指针
    while ptr!=None:
        last = before
        before = ptr
        ptr = ptr.next
        before.next = last

    ptr = before
    while ptr!=None:
        print('[%2d %6s %3d] => '%(ptr.num,ptr.name,ptr.salary),end = '')
        i += 1
        if i>=3:
            print()
            i = 0
        ptr = ptr.next

main()