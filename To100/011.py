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



