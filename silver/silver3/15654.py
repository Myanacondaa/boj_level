from itertools import permutations

n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

if m == 1:
    for ele in arr:
        print(ele)

else:
    res = list(permutations(arr, m))
    for i in range(len(res)):
        for j in range(m):
            print(res[i][j], end=' ')
        print()

