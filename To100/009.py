# day009
print('day009')

# 字符串的运算
# 字符串的拼接
s1 = 'hello'
s2 = 'world'
print(s1 + ' ' + s2)

# 重复运算
s1 = 'hello' * 3
print(s1)

# 比较运算
# 从左到右逐个字符比较
# 直接使用比较运算符来判断两个字符串的相等性或比较大小
# 字符串的大小比较比的是每个字符对应的编码的大小
s1 = 'hello'
s2 = 'World'
print(s1 >= s2)
print(s1 < s2)
print(ord('h'))
print(ord('W'))

# 成员运算
s1 = 'hell world'
print('hello' in s1)
print('world' in s1)
print('world' not in s1)

# 获取字符串长度
s1 = 'hello world'
print(len(s1))
print(len('hello world'))

# 索引和切片
s1 = 'hell world'
n = len(s1)
print(s1[2], s1[-n])
print(s1[n - 1], s1[-3])
print(s1[::3])
print(s1[2:7:2])
print(s1[2:8])

# 字符的遍历
s1 = 'hell world'
for i in range(len(s1)):
    print(s1[i])

s1 = 'hell world'
for elem in s1:
    print(elem)

# 字符串的方法
# 大小写相关操作
s1 = 'hell world'

# 字符串首字母大写
print(s1.capitalize())

# 字符串每个单词首字母大写
print(s1.title())

# 字符串变大写
print(s1.upper())

# 字符串变小写
s2 = 'THE WORLD'
print(s2.lower())

# 检查s1和s2的值
print(s1)
print(s2)

# 查找操作
# find方法找不到指定的字符串会返回-1，
# index方法找不到指定的字符串会引发ValueError错误
s1 = 'hello world'
print(s1.find('or'))
print(s1.find('or', 8))
print(s1.index('or'))
print(s1.index('or', 3))

# 逆向查找
s1 = 'hello world'
print(s1.rfind('or'))
print(s1.rfind('or'))
print(s1.rindex('or', 1))

# 性质判断
# 通过字符串的startswith、endswith来判断字符串是否以某个字符串开头和结尾
# 通过is开头的方法判断字符串的特征
# 返回布尔值
s1 = 'hello world'
print(s1.startswith('h'))
print(s1.endswith('d'))

# isdigit判断字符串是否完全由数字构成的
# isalpha用来判断字符串是否完全由字母构成的，字母指的是 Unicode 字符但不包含 Emoji 字符
# isalnum用来判断字符串是否由字母和数字构成的
s2 = 'qgmzhny123456'
print(s2.isdigit())
print(s2.isalpha())
print(s2.isalnum())

# 格式化
# center 居中
# ljust 左对齐
# rjust 右对齐
# zfill 在字符串的左侧补零
s1 = 'Hello World'
print(s1.center(20, '-'))
print(s1[:5].ljust(20, '-'))
print(s1[5:].rjust(20, '-'))
print(s1[:5].upper().ljust(20))
print(s1[5:].lower().rjust(-1).zfill(20))

# print
a = 123
b = 321
print('%d * %d = %d' % (a, b, a * b))

# format
# 按位置自动填充
# 可以重复使用
# 指定位置索引（从0开始）
# 可以改变顺序
a = 123
b = 321
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b:,}')
print(f'{a} * {b} = {a * b:.2e}')

# 修剪操作
# strip 获得将原字符串修剪掉左右两端指定字符之后的字符串，
# 默认是修剪空格字符
# lstrip
# rstrip
s1 = '     Hello World    '
print(s1.strip())
s1 = '---Hello World---'
print(s1.rstrip('-'))
print(s1.lstrip('-'))

# 替换操作
# replace 用新的内容替换字符串中指定的内容
# 参数一 被替换的内容，
# 参数二 替换后的内容，
# 参数二 指定替换的次数
s1 = 'qgmzhnyQ123456Q'
print(s1.replace('Q', '@'))
print(s1.replace('Q', '@', 1))

# 拆分与合并
# split 将一个字符串拆分为多个字符串（放在一个列表中）
# join 将列表中的多个字符串连接成一个字符串
# 默认使用空格进行拆分
# 可以指定其他的字符来拆分字符串
# 可以指定最大拆分次数来控制拆分的效果
s1 = 'qgmzhny 123456'
temp = s1.split()
print('-'.join(temp))

s1 = 'qgmzhnyQ123456'
temp = s1.split('Q')
print('@'.join(temp))

s1 = 'qgmzhnyQ123Q456Q123'
temp = s1.split('Q', 2)
print(temp)
