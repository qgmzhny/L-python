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

