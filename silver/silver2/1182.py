from itertools import combinations
# 부분 수열은 arr[a:b]가 아니라 마음대로 원소를 고르는 것임
n, s = map(int, input().split())
arr = sorted(list(map(int, input().split())))
cnt = 0

for i in range(1, n+1):
    combi = combinations(arr, i)
    for c in combi:
        if sum(c) == s:
            cnt += 1

print(cnt)