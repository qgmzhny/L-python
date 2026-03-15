# day004
print("day004")

# 分支结构

# if elif else构造分支结构
# 身体质量指数（BMI）的计算器
# 通常认为18.5≤BMI<24是正常范围，
# BMI<18.5说明体重过轻，
# BMI≥24说明体重过重，
# BMI≥27就属于肥胖的范畴
# BMI = 体重/(身高 ** 2)
# 体重以千克（kg）为单位，身高以米（m）为单位

weight = float(input('输入体重'))
height = float(input('输入身高'))
BMI = float(weight / ((height / 100) ** 2))
# BMI = float(weight / (height / 100) ** 2)
# BMI = float(weight / ((height / 100) ** 2))
print(f'{BMI = :.1f}')
print(BMI)

BMI = float(input('输入BMI'))
if BMI < 18.5:
    print('体重过轻')
elif BMI < 24:
    print('体重正常')
else:
    if BMI < 27:
        print('体重过重')
    else:
        print('肥胖')

# match和case构造分支结构
status_code = int(input('响应状态码: '))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)

# 在 Python 的 match-case 语句中，_（下划线）是一个特殊的通配符模式，表示"匹配任何东西"


status_code = int(input('响应状态码'))
match status_code:
    case 400 | 405: description = 'Invalid Request'
    case 401 | 403 | 404: description = 'Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述',description)

# python在match-case 语句中|表示或

# 分段函数求值
# if-elif-else
x = float(input('x ='))
if x < -1:
    y = 5 * x + 3
elif x <= 1:
    y = x + 2
else:
    y = 3 * x - 5
print(y)

# match-case (guard 子句/在case后面加上if条件)
x = float(input('x ='))
match x:
    case x if x < -1:
        y = 5 * x + 3
    case x if x > 1:
        y = 3 * x - 5
    case _:
        y = x + 2
print(y)



