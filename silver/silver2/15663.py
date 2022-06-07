from itertools import permutations
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
combi = sorted(set(permutations(arr, m)))

for i in combi:
    for j in i:
        print(j, end=' ')
    print()