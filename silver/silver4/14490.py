from math import gcd

n, m = map(int, input().split(':'))
a = gcd(n,m)
print(f'{int(n/a)}:{int(m/a)}')