from itertools import permutations

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
res = list(permutations(arr,m))

for ele in res:
    for i in ele:
        print(i, end=' ')
    print()