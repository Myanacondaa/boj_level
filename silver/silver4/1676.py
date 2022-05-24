from math import factorial
n = int(input())
fac = str(factorial(n))[::-1]       # 문자열 뒤집기
cnt = 0
for x in fac:        # 뒤에서부터 검사. 0이 아니면 종료
    if x != '0':
        break
    cnt += 1

print(cnt)