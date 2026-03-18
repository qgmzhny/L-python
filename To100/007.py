# day007
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


