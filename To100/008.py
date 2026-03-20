# day008
print('day008')

# 元组
# 定义
# 多个元素按照一定顺序构成的序列
# 定义后的元组的元素不能进行添加或删除的操作
# 元素的值也不能修改
# 修改元组中的元素，将引发TypeError错误

# 运算
# 定义一个三元组
t1 = (9, 5, 27)

# 定义一个四元组
t2 = ('刘德华', 66, False, '三重')

# 查看变量的类型
print(type(t1))
print(type(t2))

# 查看元组中元素的数量
print(len(t1))
print(len(t2))

# 索引运算
print(t1[2])
print(t2[2])

# 切片运算
print(t1[:2])
print(t2[::3])

# 循环遍历元组中的元素
for _ in t1:
    print(_)

# 成员运算
print(5 in t1)
print('三重' in t2)

# 拼接运算
t3 = t1 + t2
print(t3)

# 比较运算
print(t1 == t3)
print(t1 >= t3)
print(t3 <= (35, 11, 99))

# ()表示空元组
# 一元组需要加上一个逗号
# ('hello', )

# 打包
# 把多个用逗号分隔的值赋给一个变量
# 多个值会打包成一个元组类型
t1 = 'jame', 1, True
print(type(t1))
print(t1)

# 解包
# 把一个元组赋值给多个变量
# 元组会解包成多个值然后分别赋给对应的变量
a, b, c = t1
print(type(a))
print(type(b))
print(type(c))
print(a, b, c)

# 错误提示
# 如果解包出来的元素个数和变量个数不对应，
# 会引发ValueError异常，
# 错误信息为：too many values to unpack（解包的值太多）
# 或not enough values to unpack（解包的值不足）

# 星号表达式
# 通过星号表达式，
# 可以让一个变量接收多个值

# 注意事项
# 星号表达式修饰的变量会变成一个列表，
# 列表中有0个或多个元素；
# 在解包语法中，
# 星号表达式只能出现一次
temp = ('唱', '跳', 'rap', '篮球')
i, j, *k = temp
print(i, j, k)
i, *j, k = temp
print(i, j, k)
i, j, k, l = temp
print(i, j, k, l)
i, j, k, l, *m = temp
print(i, j, k, l, m)

# range函数构造的范围序列甚至字符串都可以使用解包语法
a, b, *c = range(10)
print(a, b, c)
a, b, c = [1, 5, 10]
print(a, b, c)
a, *b, c = 'hello world'
print(a, b, c)

# 交换变量的值
a = 1
b = 2
a, b = b, a
print(a, b)

# 将三个变量a、b、c的值互换，
# b的值赋给a，c的值赋给b，a的值赋给c
a = 1
b = 2
c = 3
a, b, c = b, c, a
print(a, b, c)

# 多于三个变量的值要依次互换
# 需要通过打包解包的方式来完成变量之间值的交换

# 元组和列表的比较
# 元组是不可变类型，
# 通常不可变类型在创建时间上优于对应的可变类型

# 分别创建了保存1到9的整数的列表和元组，
# 每个操作执行10000000次，统计运行时间
import timeit
print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

# Python 中的元组和列表类型是可以相互转换
temp = ('唱', '跳', 'rap', '篮球')
# 将元组转换成列表
print(list(temp))
nums1 = [35, 12, 97, 64, 55]
print(tuple(nums1))

# 字符串
# 我们把单个或多个字符用单引号或者双引号包围起来，
# 表示一个字符串
s1 = '''hello,
wonderful
world!'''
s2 = "你好，世界！❤️"
print(s1)
print(s2)

