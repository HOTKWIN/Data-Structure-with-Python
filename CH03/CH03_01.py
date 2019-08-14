# 遍历单链表

import sys

class student:
    def __init__(self):
        self.name = ''
        self.Math = 0
        self.Eng = 0
        self.no = ''
        self.next = None

"""写入链表"""
# 建立链表的头部
head = student()
head.next = None
ptr = head
Msum = Esum = num = student_no = 0
select = 0

while select !=2:
    print('(1)新增 (2)离开 =>')
    try:
        select = int(input('请输入一个选项: '))
    except ValueError:
        print('输入错误')
        print('请重新输入\n')
    if select == 1:
        # 新增下一个元素
        new_data = student()
        new_data.name = input('姓名:')
        new_data.no = input('学号:')
        new_data.Math = eval(input('数学成绩:'))
        new_data.Eng = eval(input('英语成绩:'))
        # 存取指针设置为新元素所在位置
        ptr.next = new_data
        # 新元素的next先设置为None
        new_data.next = None
        ptr = ptr.next
        num += 1

"""读取链表"""
# 存取指针从链表头部开始
ptr = head.next
print()
while ptr != None:
    print('姓名:%s\t学号:%s\t数学成绩:%d\t英语成绩:%d'%(ptr.name,ptr.no,ptr.Math,ptr.Eng))
    Msum = Msum+ptr.Math
    Esum = Esum+ptr.Eng
    student_no += 1
    # 存取指针移往下一个元素
    ptr = ptr.next

if student_no !=0:
    print('-'*50)
    print('本链表中学生的数学平均成绩:%.2f 英语平均成绩:%.2f'%(Msum/student_no,Esum/student_no))