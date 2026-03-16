# day005
import time

print("day005")

# 循环结构
# for-in循环
# 明确知道循环执行的次数

# import time
for i in range(40):
    print('hello world!')
    time.sleep(1)

# range 对象并不存储每一个数字
# 它存储的是 起始值、结束值和步长
# range(40)：可以用来产生0到39范围的整数，取不到40
# sleep 单位是s

# Python 的编程惯例，我们通常把循环变量命名为 _
# import time
for _ in range(40):
    print('hello world!')
    time.sleep(0.1)

# 用for-in循环实现从 1 到 100 的整数求和
s = 0
for _ in range(1, 101):
    s += _
print(f's = {s}')

# 从1到100偶数求和
total  = 0
for _ in range(0, 101, 2):
    print(_)
    total += _
print(f'total = {total}')

print(sum(range(2,101,2)))

# while循环
# 不能确定循环重复的次数

# 从1到100的偶数求和
total = 0
i = 1
while i < 101:
    total += i
    i += 1
print(f'total = {total}')

# break
total = 0
i = 1
while True:
    total += i
    i += 1
    if i > 100:
        break
print(f'total = {total}')

