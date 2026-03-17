# day006
print("day006")

# 100以内的素数
for _ in range(2, 100):
    prime_status = True
    half_factor = int(_ ** 0.5)
    for i in range(2, half_factor + 1):
        if _ % i == 0:
            prime_status = False
            break
    if prime_status:
        print(f'{_}是素数')
    else:
        print(f'{_}不是素数')

# 斐波那契数列
# 输出斐波那契数列中的前 20 个数
# 斐波那契数列的特点是数列的前两个数都是 1，从第三个数开始，每个数都是它前面两个数的和

f1 = 1
f2 = 1
print(f'f1 = {f1}')
print(f'f2 = {f2}')
for i in range(1, 19):
    fn = f1 + f2
    temp = fn
    f1 = f2
    f2 = temp
    print(f'f{i + 2} = {fn}')

# a, b = 0, 1
# for _ in range(20):
#     a, b = b, a + b
#     print(a)

# 寻找水仙花数
# 找出 100 到 999 范围内的所有水仙花数
# 水仙花数:
# 一个 N位非负整数，
# 其各位数字的N次方和刚好等于该数本身
for _ in range(100, 1000):
    b3 = int(_ / 100)
    b2 = int((_ - 100 * b3) / 10)
    b1 = _ - 100 * b3 - 10 * b2
    if b1 ** 3 + b2 ** 3 + b3 ** 3 == _:
        print(f'{_}是水仙花数')

# for num in range(100, 1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)

# // 为整除符号


