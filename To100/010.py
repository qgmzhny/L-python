# day010
print('day010')

# 集合（set）
# 一定范围的、确定的、可以区别的事物当作一个整体来看待
# 集合中的各个事物称为集合的元素
# 要求
# 无序性：一个集合中，每个元素的地位都是相同的，元素之间是无序的
# 互异性：一个集合中，任何两个元素都是不相同的，即元素在集合中只能出现一次
# 确定性：给定一个集合和一个任意元素，该元素要么属这个集合，要么不属于这个集合

# 创建集合
# 创建集合可以使用{}字面量语法，
# {}中需要至少有一个元素，
# 没有元素的{}并不是空集合而是一个空字典

nums = {1, 2, 3, 4, 3, 2, 1}
print(nums)

ikun = {'唱', '跳', 'rap', '篮球'}
print(ikun)

set1 = set('hello')
print(set1)

set2 = set([1 , 2, 3, 3, 4])
print(set2)

set3 = {num for num in range(1, 100) if num % 17 == 0 and num // 7 < 50}
print(set3)

# 集合中的元素必须是hashable类型
# 通常不可变类型都是hashable类型
# 可变类型都不是hashable类型
# 能够计算出哈希码的数据类型
# 集合不能作为集合中的元素

# 元素的遍历
# 不能通过索引运算来遍历集合中的元素
ikun = {'唱', '跳', 'rap', '篮球'}
for elem in ikun:
    print(elem)

# 集合的运算
# 成员运算
ikun = {'唱', '跳', 'rap', '篮球'}
print('唱' in ikun)
print('music' not in ikun)

# 二元运算
# 交集、并集、差集、对称差
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
print(set1 & set2)
print(set1.intersection(set2))

# 并集
print(set1 | set2)
print(set1.union(set2))

# 差集
print(set1 - set2)
print(set2 - set1)
print(set1.difference(set2))
print(set2.difference(set1))

# 对称差
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# 集合的二元运算还可以跟赋值运算一起构成复合赋值运算
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}
set1 |= set2    # <==> set1.update(set2)
print(set1)

set3 = {3, 6, 9}
set1 &= set3    # <==> set1.intersection_update()
print(set1)

set2 -= set1    # <==> set2.difference_update()
print(set2)
set1 &= set2
print(set1)

# 比较运算
# 超集：B集合 包含 A集合 的所有元素（B 可以等于 A）
# 真超集：B 包含 A 的所有元素，且 B ≠ A（严格包含）
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {1, 3, 5, 7}
set3 = {2, 3, 5, 7}

print(set2 < set1)
print(set2 <= set1)
print(set3 < set1)
print(set3 <= set1)
print(set1 > set2)
print(set1 >= set2)

print(set2.issubset(set1))
print(set1.issuperset(set2))



