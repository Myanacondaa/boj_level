from math import factorial
n, k = map(int, input().split())
print(int(factorial(n-1)/(factorial(k-1)*factorial(n-k))))