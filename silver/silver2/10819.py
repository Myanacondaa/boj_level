from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
maximum = -1

for p in permutations(arr, n):
    res = 0
    for i in range(n-1):
        res += abs(p[i]-p[i+1])
    maximum = max(maximum, res)

print(maximum)
