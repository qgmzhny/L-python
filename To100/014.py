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
