import random
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