from math import gcd
a, b = map(int, input().split())

# 두 수의 1의 개수의 최대 공약수만이 두 수의 최대공약수
# 예) a = 3, b = 4 gcd(3, 4) = 1, 따라서 111과 1111의 gcd는 1
# 예2) a= = 3, b = 6 gcd(3,6) = 3, 따라서 111과 111111의 gcd는 '1'*3

print('1'*gcd(a,b))