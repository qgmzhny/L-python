import string

# day013函数应用
print('day013')

# 随机验证码
# 设计一个生成随机验证码的函数，
# 验证码由数字和英文大小写字母构成，
# 长度可以通过参数设置

# import random
# import string
ALL_CHARS = string.digits + string.ascii_letters
def VerCode(*, code_len = 4):

    return ''.join(random.choices(ALL_CHARS, k= code_len))


for _ in range(5):
    print(VerCode())

# import random
def generate_code(*, args ):
    nums = list(range(10))
    symbol = [chr(i) for i in list(range(97, 123)) + list(range(65, 91))]
    return (''.join(str(_) for _ in random.choices(nums + symbol, k= args)))


print('参数个数：')
print(generate_code(args = int(input())))


# 判断素数
# 设计一个判断给定的大于1的正整数是不是质数的函数。
# 质数是只能被1和自身整除的正整数（大于1），
# 如果一个大于 1 的正整数N是质数，
# 那就意味着在 2 到 N−1之间都没有它的因子

def is_prime(num):
    if num <= 1:
        return 0
    elif num == 4:
        return 1
    else:
        for _ in range(2, num // 2):
            if num % _ == 0:
                return 1
    return 2

def ST_Judge(num):
    if num == 0:
        print('数据需要大于1的整数')
    elif num == 1:
        print('是合数')
    else:
        print('是质数')


print('请输入需要判断的数据')
num = int(input())
temp = is_prime(num)
ST_Judge(temp)

def is_prime(num) -> bool:
    for _ in range(2, int(num ** 0.5) + 1):
        if num % _ == 0:
            return False

    return True


print('请输入需要判断的数据')
num = int(input())

if(is_prime(num)):
    print('质数')
else:
    print('合数')


# 最大公约数和最小公倍数
# 计算两个正整数最大公约数和最小公倍数的函数
def gcd(num1, num2) -> int:
    """求最大公约数"""
    return num1 if num2 == 0 else gcd(num2, num1 % num2)


def lcm(num1, num2) -> int:
    """求最小公倍数"""
    return num1 * num2 // gcd(num1, num2)


print('请输入需要计算的数据')
num1 = int(input())
num2 = int(input())
print(
    f'{num1}和{num2}的最大公约数为：{gcd(num1, num2)};\t最小公倍数为：{lcm(num1, num2)}'
)


# 数据统计


# 双色球随机选号
# 将生成随机号码和输出一组号码的功能分别封装到两个函数中，
# 通过调用函数实现机选N注号码的功能

# 双色球是由中国福利彩票发行管理中心发售的乐透型彩票，
# 每注投注号码由6个红色球和1个蓝色球组成。
# 红色球号码从1到33中选择，
# 蓝色球号码从1到16中选择。
# 每注需要选择6个红色球号码和1个蓝色球号码

import random


def generate_balls() -> list:
    red_ball = [i for i in range(1, 34)]
    blue_ball = [i for i in range(1, 17)]
    win_ball = []
    for _ in range(6):
        win_ball.append(random.choice(red_ball))
    win_ball.append(random.choice(blue_ball))
    return win_ball


def show_numbers(nums: int):
    for _ in range(nums):
        win_balls = generate_balls()
        last = win_balls.pop()
        # 输出选中的红色球
        for ball in win_balls:
            print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
        # 输出选中的蓝色球
        print(f'\033[034m{last:0>2d}\033[0m')


# 买奖
print('生成几注号码: ')
nums = int(input())
# 开奖
show_numbers(nums)

