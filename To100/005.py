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

# continue
total = 0
i = 1
while True:
    total += i
    i += 1
    if i < 101:
        continue
    break

print(f'total = {total}')

# 嵌套的循环结构
# 九九乘法口诀表
# 下三角
for _ in range(1, 10):
    i = 1
    while i < (_ + 1):
        print(f'{i}×{_}={i * _}', end='\t')
        i += 1
    print()

# end 是 print() 函数的可选参数

# 上三角
for _ in range(1, 10):
    i = 1
    while i < 10:
        if i < _:
            print(f'\t\t', end='')
        else:
            print(f'{_}×{i}={i * _}', end='\t')
        i += 1
    print()

# 判断素数
# 输入一个大于 1 的正整数，判断它是不是素数。
prime = int(input('输入一个大于 1 的正整数:'))
if prime <= 1:
    print('非法输入')
else:
    if prime == 2:
        print(f'{prime}是素数')
    else:
        for _ in range(2, prime):
            if prime % _ == 0:
                print(f'{prime}不是素数')
                break
            if prime == _ + 1:
                print(f'{prime}是素数')

# 对于大于 1 的正整数，因子应该都是成对出现的，所以循环到(n ** 0.5)就可以结束了
prime = int(input('输入一个大于 1 的正整数:'))
half = int(prime ** 0.5)
# int()向0取整
if prime == 2 or prime == 3:
    print(f'{prime}是素数')
else:
    for _ in range(2, half + 1):
        if prime % _ == 0:
            print(f'{prime}不是素数')
            break
        else:
            print(f'{prime}是素数')

# num = int(input('请输入一个正整数: '))
# end = int(num ** 0.5)
# is_prime = True
# for i in range(2, end + 1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(f'{num}是素数')
# else:
#     print(f'{num}不是素数')

# 最大公约数
# 输入两个大于 0 的正整数，求两个数的最大公约数
num1 = int(input('输入两个大于 0 的正整数'))
num2 = int(input('输入两个大于 0 的正整数'))
if num1 < 0 or num2 < 0:
    print('无效输入')
else:
    for share_nums in range(num1, 0, -1):
        if num1 % share_nums == 0 and num2 % share_nums == 0:
            print(f'最大公约数: {share_nums}')

