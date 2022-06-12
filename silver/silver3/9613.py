from math import gcd
t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    gcd_set = []
    for i in range(len(a)):
        for j in range(1, i):
            gcd_set.append(gcd(a[i], a[j]))

    print(sum(gcd_set))