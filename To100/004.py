# day004
print("day004")

# 分支结构

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

