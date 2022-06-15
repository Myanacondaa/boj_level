from math import factorial
# 만약 세자리(xyz)일 경우 오르막 수 : x <= y<= z  >> 중복 조합
# nHr = n+r-1Cr
# 0부터 9까지의 수 중 중복을 허용하여 n개를 뽑음
# 10Hn = 10+n-1Cn = 9+nCn
n = int(input())
print(int(factorial(9+n)//(factorial(9)*factorial(n))) % 10007)

