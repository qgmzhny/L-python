# day007
import random

print("day007")

# 常用数据结构

# 列表
# 用一个变量来保存多个数据
# 统一的代码对多个数据进行操作

# 列表（list）
# 在 Python 中
# 使用[]字面量语法来定义列表
# 列表中的多个元素用逗号进行分隔

items1 = [9, 5, 2, 7]
items2 = ['list', 'for-in', 'while']
items3 = [101, 'jack', False]
print(items1)
print(items2)
print(items3)
print(type(items1))
print(type(items2))
print(type(items3))

# list函数将其他序列变成列表
items4 = list(range(1, 10))
print(items4)
items5 = list('hello world!')
print(items5)

# 列表运算
# 使用+运算符拼接列表
items6 = [35, 12, 99, 45, 66]
items7 = ['python', 'java', 'c']
items8 = [True, False]
print(items6 + items8)
print(items7 + items8)
items6 += items7
print(items6)

# 使用*运算符重复运算
# *运算符会将列表元素重复指定的次数
items6 = [35, 12, 99, 45, 66]
items7 = ['python', 'java', 'c']
print(items6 * 3)
print(items7 * 3)

# 成员运算符in, not in
# 使用in或not in运算符判断一个元素在不在列表中
items6 = [35, 12, 99, 45, 66]
items7 = ['python', 'java', 'c']
print(5 in items6)
print(6 not in items6)
print('c' in items7)
print('c++' not in items7)

# []运算符
# []的元素位置
# 0到N - 1的整数
# -1到-N的整数(负数索引)
items9 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items9[3])
print(items9[0])
items9[4] = 'tom'
print(items9)
print(items9[-2])
print(items9[-3])
items9[-4] = 'strawberry'
print(items9)

# 切片运算
items9 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items9[:: 2])
print(items9[1:: 3])
print(items9[: 3: 2])
print(items9[0: 4: 1])
print(items9[1:: -1])
print(items9[-1: -5: -1])

# 通过切片操作修改列表中的元素
items9 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
items9[1:3] = ['ik', 'un', '!']
print(items9)

# 关系运算
# 比较两个列表是否相等，
# 比较两个列表大小(比较第一个不同元素的大小)
nums1 = [1, 2, 3, 4]
nums2 = list(range(1, 5))
nums3 = [3, 2, 1]
print(nums1 == nums2)
print(nums1 != nums2)
print(nums1 >= nums3)
print(nums2 <= nums3)

# 元素的遍历
# 索引运算
# 使用 [] 来访问序列（列表、字符串、元组等）中特定位置元素的操作
items9 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
for _ in range(len(items9)):
    print(items9[_], end='\t')

# len函数
# 可以获取列表元素的个数N
# range(N)则构成了从0到N-1的范围
items9 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
index = 0
while index != len(items9):
    print(items9[index])
    index += 1

items9 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
for items9 in items9:
    print(items9)

# 掷色子统计每种点数出现次数
# import random
# 色子列表
counter = []

# 色子点数
f = [0, 0, 0, 0, 0, 0]

for index in range(60):
    counter.append(random.randrange(1, 7))
for _ in range(60):
    if counter[_] == 1:
        f[0] += 1
    elif counter[_] == 2:
        f[1] += 1
    elif counter[_] == 3:
        f[2] += 1
    elif counter[_] == 4:
        f[3] += 1
    elif counter[_] == 5:
        f[4] += 1
    else:
        f[5] += 1

for f in f:
    print(f)

# import random
# 色子点数
f = [0] * 6
for index in range(60):
    counter = random.randrange(1, 7)
    f[counter - 1] += 1

for index in range(6):
    print(f'{index + 1}点出现了{f[index - 1]}次')

# 列表的方法
# 给对象发消息
# 通过对象引用调用对象方法

# 添加和删除元素

# 添加
# append方法向列表中追加元素
# insert方法向列表中插入元素

# 追加
fruit = ['apple', 'banana', 'orange', 'strawberry', 'grape']
print(fruit)

# 插入
fruit.insert(2, 'mango')
print(fruit)

# 删除元素
fruits = ['apple', 'banana', 'mango', 'orange', 'strawberry', 'grape']
if 'apple' in fruits:
    fruits.remove('apple')
if 'Java' in fruits:
    fruits.remove('Java')
print(fruits)

# list.pop()
fruits.pop()
temp = fruits.pop(1)
print(temp)
fruits.append(temp)
print(fruits)

# list.clear()
fruits.clear()
print(fruits)



