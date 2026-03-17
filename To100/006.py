# day006

import random

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

# 正整数的反转
num = int(input('num ='))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(f'reversed_num = {reversed_num}')

# 百钱百鸡问题
# 鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？

# (分析)==>
# x1 > 0 and x1 < 20,
# x2 > 0 and x2 < 34,
# x3 > 0 and x3 < 100 < 300
# x1 + x2 + x3 == 100
# x1*n1 + x2*n2 + x3*n3 == 100

for x1 in range(0, 21):
    for x2 in range(0, 34):
        for x3 in range(0, 100):
            if 5 * x1 + 3 * x2 + x3 // 3 == 100 and x1 + x2 + x3 == 100 and x3 % 3 == 0:
                print(f'x1 = {x1}', end='\t')
                print(f'x2 = {x2}', end='\t')
                print(f'x3 = {x3}', end='\t')
                print()

# for x in range(0, 21):
#     for y in range(0, 34):
#         for z in range(0, 100, 3):
#             if x + y + z == 100 and 5 * x + 3 * y + z // 3 == 100:
#                 print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')

# CRAPS赌博游戏
# 使用两粒骰子,获得点数进行游戏
# 玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；
# 玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
# 玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果玩家摇出了 7 点，庄家胜；
# 如果玩家摇出了第一次摇的点数，玩家胜；
# 其他点数玩家继续摇骰子，直到分出胜负

# 开始时玩家有 1000 元的赌注，
# 每局游戏开始之前，玩家先下注，
# 如果玩家获胜就可以获得对应下注金额的奖励，
# 如果庄家获胜，玩家就会输掉自己下注的金额。
# 游戏结束的条件是玩家破产

# import random
# 初始资金
initial_capital = 10

# 开盘次数
num = 0

# 打印表头
print("下注金额\t开盘点数\t首次点数\t结果\t\t剩余资金")
print("-" * 60)

while initial_capital > 0:
    # 玩家下注
    bet = random.randint(1, initial_capital)

    # 开盘
    guess_total = random.randint(1, 6) + random.randint(1, 6)
    num += 1

    if num == 1:
        # 记录第一次开盘骰子数
        first_guess = guess_total

        if guess_total == 7 or guess_total == 11:
            initial_capital += bet
            result = "玩家胜"
        elif guess_total == 2 or guess_total == 3 or guess_total == 12:
            initial_capital -= bet
            result = "庄家胜"
        else:
            initial_capital = initial_capital
            result = "继续游戏"
    else:
        if guess_total == first_guess:
            initial_capital += bet
            result = "玩家胜"
        elif guess_total == 7:
            initial_capital -= bet
            result = "庄家胜"
        else:
            initial_capital = initial_capital
            result = "继续游戏"

    # 统一输出，每列宽度8个字符，左对齐
    print(f"{bet}\t\t{guess_total}\t\t{first_guess}\t\t{result}\t\t{initial_capital}")

print("-" * 60)
print(f"游戏结束！共开盘{num}次，已破产")
