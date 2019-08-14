# 矩阵相乘
"""
实现可自行输入矩阵维数的矩阵相乘的过程，并显示输出相乘后的结果
"""

def MatrixMultiply(arrA,arrB,arrC,M,N,P):
    global C
    if M<=0 or N<=0 or P<=0:
        print('错误:维数必须大于0')
        return
    for i in range(M):
        for j in range(P):
            Temp = 0
            for k in range(N):
                Temp = Temp + int(arrA[i*N+k])*int(arrB[k*P+j])
            arrC[i*P+j] = Temp

print('请输入矩阵A的维数(M,N):')
M = int(input('M= '))
N = int(input('N= '))
A = [None]*M*N

print('请输入矩阵A的各个元素:')
for i in range(M):
    for j in range(N):
        A[i*N+j] = input('a%d%d='%(i,j))

print('请输入矩阵B的维数(N,P):')
N = int(input('N= '))
P = int(input('P= '))
B = [None]*N*P

print('请输入矩阵B的各个元素:')
for i in range(N):
    for j in range(P):
        B[i*P+j] = input('b%d%d='%(i,j))

C = [None]*M*P
MatrixMultiply(A,B,C,M,N,P)
print('AxB的结果是:')
for i in range(M):
    for j in range(P):
        print('%d'%C[i*P+j],end = '\t')
    print()