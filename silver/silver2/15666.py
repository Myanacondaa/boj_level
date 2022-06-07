from itertools import combinations_with_replacement

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
combi = sorted(set(combinations_with_replacement(arr, m)))

for i in combi:
    for j in i:
        print(j, end=' ')
    print()