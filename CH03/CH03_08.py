# 环形链表的建立与遍历
"""
设计程序，让用户输入数据来新增学生数据节点，并建立一个环形链表，当用户输入结束后，可遍历此链表并显示其内存
"""

class student:
    def __init__(self):
        self.name = ''
        self.no = ''
        self.next = None

# 新增链表头元素
head = student()
ptr = head
ptr.next = None

select = 0
while select != 2:
    select = int(input('(1)新增 (2)离开 =>'))
    if select == 2:
        break
    ptr.name = input('姓名: ')
    ptr.no = input('学号: ')
    # 新增下一个元素
    new_data = student()
    ptr.next = new_data
    new_data.next = None
    ptr = new_data

ptr.next = head
print()
ptr = head

while True:
    print('姓名: %s\t学号:%s\n'%(ptr.name,ptr.no))
    ptr = ptr.next
    if ptr.next == head:
        break