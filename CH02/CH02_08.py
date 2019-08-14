# 上三角矩阵
"""
将右上三角矩阵压缩为一维数组
"""

global ARRAY_SIZE # 矩阵维数大小
ARRAY_SIZE = 5

# 一维数组声明
num = int(ARRAY_SIZE*(1+ARRAY_SIZE)/2)
B = [None]*num

def getValue(i,j):
    index = int(ARRAY_SIZE*i - i*(i+1)/2 + j)
    return B[index]

# 上三角内容
A = [[7,8,12,21,9],
     [0,5,14,17,6],
     [0,0,7,23,24],
     [0,0,0,32,19],
     [0,0,0,0,8]]
print('='*30)
print('上三角矩阵:')
for i in range(ARRAY_SIZE):
    for j in range(ARRAY_SIZE):
        print('%d'%A[i][j],end = '\t')
    print()

# 将上三角矩阵压缩为一维数组
index = 0
for i in range(ARRAY_SIZE):
    for j in range(ARRAY_SIZE):
        if (A[i][j]!=0):
            B[index] = A[i][j]
            index += 1

print('='*30)
print('以一维数组的方式表示:')
print(B)