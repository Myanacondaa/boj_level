import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

s = sum(arr)
ans = 0
for n in arr:
    s -= n
    ans += n * s

print(ans)