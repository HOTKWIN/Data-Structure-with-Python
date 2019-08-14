# 数组与多项式
"""
进行两个多项式的加法运算
"""

# 将两个最高次方相等的多项式相加后输出结果
ITEMS = 6
def PrintPoly(Poly):
    MaxExp = Poly[0]
    for i in range(1,Poly[0]+2):
        MaxExp -= 1
        if Poly[i] != 0:
            if (MaxExp+1)!=0:
                print(' %dX^%d'%(Poly[i],MaxExp+1),end = '')
            else:
                print(' %d'%Poly[i],end = '')
            if MaxExp>=0:
                print('%c'%'+',end='')
    print()

def PolySum(Poly1,Poly2):
    result = [None]*ITEMS
    result[0] = Poly1[0]
    for i in range(1,Poly1[0]+2):
        result[i] = Poly1[i]+Poly2[i]
    PrintPoly(result)

PolyA = [4,3,7,0,6,2]
PolyB = [4,1,5,2,0,9]
# 打印出多项式A
print('多项式A=>',end = '')
PrintPoly(PolyA)
# 打印出多项式B
print('多项式B=>',end = '')
PrintPoly(PolyB)
# 多项式A+多项式B
print('多项式A+B=>',end = '')
PolySum(PolyA,PolyB)