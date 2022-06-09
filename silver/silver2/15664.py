from itertools import combinations


n, m = map(int, input().split())

arr = sorted(list(map(int, input().split())))

combi = sorted(set(combinations(arr, m)))

for ele in combi:
    for j in ele:
        print(j, end=' ')
    print()

