# day006
print("day006")

# 100以内的素数
for _ in range(2, 100):
    prime_status = True
    half_factor = int(_ ** 0.5)
    for i in range(2, half_factor + 1):
        if _ % i == 0:
            prime_status = False
            break
    if prime_status:
        print(f'{_}是素数')
    else:
        print(f'{_}不是素数')




