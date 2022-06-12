from itertools import combinations_with_replacement
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

combi = list(combinations_with_replacement(arr, m))

for ele in combi:
    for i in ele:
        print(i, end=' ')
    print()
