# day011
print('day011')

# 字典
# 以键值对（键和值的组合）的方式把数据组织到一起

# 创建和使用字典
hobby = {
    '唱': 'ikun一艺',
    '跳': 'ikun二艺',
    'rap': 'ikun三艺',
    '篮球': 'ikun四艺'
}
print(hobby)

person = {
    'name': '鸽鸽',
    'age': 2.5,
    'fans': 'ikun',
    'identity': '宗主',
    'festival': 'KFC，疯狂星期四',
    'prices': '50 dollars'
}
print(person)

person = dict(
    name = '鸽鸽',
    age = 2.5,
    fans = 'ikun',
    identity = '宗主',
    festival = 'KFC，疯狂星期四',
    prices = '50 dollars'
)
print(person)

items1 = dict(zip('abcdef', '123456'))
print(items1)

items2 = dict(zip('abcd', range(1, 6)))
print(items2)

items3 = {x: x ** 3 for x in range(1, 6)}
print(items3)

# 查询键值对数量
hobby = {
    '唱': 'ikun一艺',
    '跳': 'ikun二艺',
    'rap': 'ikun三艺',
    '篮球': 'ikun四艺'
}
print(len(hobby))
for _ in hobby:
    print(_)

# 字典的运算
# 字典中的键必须是不可变类型
person = dict(
    name = '鸽鸽',
    age = 2.5,
    fans = 'ikun',
    identity = '宗主',
    festival = 'KFC，疯狂星期四',
    prices = '50 dollars',
    hobby = {
        '唱': 'ikun一艺',
        '跳': 'ikun二艺',
        'rap': 'ikun三艺',
        '篮球': 'ikun四艺'
    }
)
print(person)

# 成员运算
print('hobby' in person)
print('music' in person)

# 索引运算
print(person['hobby'])

# 循环遍历
for _ in person:
    print(f'{_}:\t{person[_]}')

# 指定的键没有在字典中，将会引发KeyError异常



