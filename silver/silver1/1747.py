from math import sqrt


def is_prime(x: int):        # 소수인지 판별
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


n = int(input())
for i in range(n, 1000001):
    if i == 1:      # 1을 펠린드롬수이면서 소수로 판단할 수 있기 때문에 따로 예외처리
        continue

    if str(i) == str(i)[::-1]:      # 펠린드롬수 이면
        if is_prime(i):     # 펠린드롬수이고 소수이면
            print(i)
            exit(0)

print(1003001)      # 100만 이상의 소수이면서 펠린드롬수

