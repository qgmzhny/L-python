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
def generate_code(*, args):
    nums = list(range(10))
    symbol = [chr(i) for i in list(range(97, 123)) + list(range(65, 91))]
    return (''.join(str(_) for _ in random.choices(nums + symbol, k= args)))


print('参数个数：')
print(generate_code(args = int(input())))


