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

from math import factorial
m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n) // factorial(m - n))



