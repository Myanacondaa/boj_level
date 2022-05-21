# 문제 답 잘못됨
# 내가 맞음
from math import lcm
n = int(input())
a = list(map(int, input().split()))
if len(a) == 1:
    print(a[0]*2)

elif len(a) == 2:
    result = lcm(a[0], a[1])
    if result == max(a):
        print(result*2)
    else:
        print(result)

else:
    a.sort()
    result = lcm(a[0], a[1])
    for i in range(2, len(a)):
        result = lcm(result, a[i])

    if result == a[-1]:
        print(result*2)
    else:
        print(result)