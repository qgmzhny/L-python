# day014函数应用
print('day014')

# 高阶函数
# Python 中函数
# 可以赋值给变量，
# 可以作为函数的参数，
# 可以作为函数的返回值。
# 去掉一个整数列表中的奇数，并对所有的偶数求平方得到一个新的列表


def is_even(num) -> bool:
    """判断num是不是偶数"""
    return num % 2 == 0


def square(num) -> int:
    """求平方"""
    return num ** 2


old_nums = [9, 5, 2, 7, 6, 3, 8]
new_nums = list(map(square, filter(is_even, old_nums)))
print(new_nums)

old_nums = ['唱', '跳', 'rap', '篮球']
new_nums = sorted(old_nums)
print(new_nums)

old_nums = ['唱', '跳', 'rap', '篮球']
new_nums = sorted(old_nums, key= len)
print(new_nums)

# Lambda函数
# 匿名函数
# 代码中的表达式产生的运算结果就是这个匿名函数的返回值

# 使用高阶函数的时候
# 作为参数或者返回值的函数本身非常简单，一行代码就能够完成
# 不需要考虑对函数的复用
old_nums = [9, 5, 2, 7, 6, 3, 8]
new_nums = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums))
print(list(new_nums))
print(list(old_nums))

# 如果传入的序列中所有的布尔值都是True，all函数返回True，否则all函数返回False
# 用一行代码实现判断素数的函数
is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))
print(is_prime(37))

# 计算及格分数的平均分
# 1. 过滤：只保留及格分数(>=60)  (filter)
# 2. 映射：每个分数加5分（平时分）  (map)
# 3. 归约：计算平均分  (reduce)
from functools import reduce
scores = [85, 92, 78, 90, 88, 45, 95, 60]
news = reduce(lambda x, y: x + y,
              map(lambda x: x + 5,
                  filter(lambda x: x >= 60, scores)))

print(news)

# 偏函数
# 函数的某些参数，生成一个新的函数，
# 就无需在每次调用函数时都传递相同的参数
# 可以使用functools模块的partial函数来创建偏函数
import functools

int2 = functools.partial(int, base = 2)
int8 = functools.partial(int, base = 8)
int16 = functools.partial(int, base = 16)
print(int('1001'))
print(int2('1001'))
print(int8('1001'))
print(int16('1001'))
print(type(int))

# partial函数的第一个参数和返回值都是函数，它将传入的函数处理成一个新的函数返回
