# 三维数组
"""
利用三重嵌套循环找出2x3x3三维数组中所有存储数值中的最小值
"""

# 声明三维数组
num = [[[33,45,67],
        [23,71,66],
        [55,38,66]],

       [[21,9,15],
        [38,69,18],
        [90,101,89]]]
# 设置value为num数组的第一个元素
value = num[0][0][0]
for i in range(2):
    for j in range(3):
        for k in range(3):
            if (value>=num[i][j][k]):
                value = num[i][j][k]
print('最小值 = %d'%value)