from math import factorial
from random import randrange

# day012
print('day012')

# 函数和模块
# 组合数计算
m = int(input('m = '))
n = int(input('n = '))
fm = 1
fn = 1
temp = 1
# 计算m的阶乘
for _ in range(1, m + 1):
    fm *= _
print(f'm = {fm}')

# 计算n的阶乘
for _ in range(1, n + 1):
    fn *= _
print(f'n = {fn}')

# 计算|m-n|的阶乘
for _ in range(1, m - n + 1):
    temp *= _
print(f'temp = {temp}')

# 计算组合数
print(f"C({m}, {n}) = {fm // (fn * temp)}")


# 定义函数
# 输入m和n，计算组合数C(m,n)的值
def fac(num):
    result = 1
    for _ in range(2, num + 1):
        result *= _
    return result


m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n) // fac(m - n))

# from math import factorial
m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n) // factorial(m - n))


# 函数的参数
# 根据给出的三条边的长度判断是否可以构成三角形，
# 可以构成三角形则返回True，否则返回False
def make_judgement(a, b, c):
    """判断三条边的长度能否构成三角形"""
    if a + b > c and a + c > b:
        return True
    return False


a = int(input('a = '))
b = int(input('a = '))
c = int(input('a = '))
print(make_judgement(a, b, c))
print(make_judgement(b= 2, a= 3, c=4))

# 可以在参数列表中用/设置强制位置参数,调用函数时只能按照参数位置来接收参数值的参数
# / 左边：只能位置传
def make_judgement(a, b, c, /):
    """判断三条边的长度能否构成三角形"""
    if a + b > c and a + c > b:
        return True
    return False


print(make_judgement(2, 3, 4))


# 用*设置命名关键字参数,只能通过“参数名=参数值”的方式来传递和接收参数
# * 右边：只能关键字传
def make_judgement(*, a, b, c):
    """判断三条边的长度能否构成三角形"""
    if a + b > c and a + c > b:
        return True
    return False


print(make_judgement(b= 2, a= 3, c=4))

# 参数的默认值
# Python 中允许函数的参数拥有默认值
# CRAPS游戏
# 定义摇色子的函数
# 函数的自变量（参数）n表示色子的个数，默认值为2
# 函数的因变量（返回值）表示摇n颗色子得到的点数

# from random import randrange
def roll_dice(n = 2):
    total = 0
    for _ in range(n):
        total += randrange(1, 7)
    return total


# 如果没有指定参数，那么n使用默认值2，表示摇两颗色子
print(roll_dice())
# 传入参数3，变量n被赋值为3，表示摇三颗色子获得点数
print(roll_dice(3))

def add(a = 0, b = 0, c = 0):
    """三个数相加求和"""
    return a + b + c


print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))

# 带默认值的参数必须放在不带默认值的参数之后

# 可变参数
# 通过星号表达式语法让函数支持可变参数
# 在调用函数时，可以向函数传入0个或任意多个参数

# 对任意多个数求和的add函数
# 用星号表达式来表示args可以接收0个或任意多个参数
# 调用函数时传入的n个参数会组装成一个n元组赋给args
# 如果一个参数都没有传入，那么args会是一个空元组
def add(*args):
    total = 0
    for _ in args:
        if type(_) in (int, float):
            total += _
    return total


print(add(1, 2, 'hello', 3.45, 6))

# 通过“参数名=参数值”的形式传入若干个参数
# 参数列表中的**kwargs可以接收0个或任意多个关键字参数
# 调用函数时传入的关键字参数会组装成一个字典（参数名是字典中的键，参数值是字典中的值）
# 如果一个关键字参数都没有传入，那么kwargs会是一个空字典
def foo(*args, **kwargs):
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')


foo(2.5, 50, name ='ikun', age = '练习时长两年半', hobby = '唱,跳,rap,篮球')






