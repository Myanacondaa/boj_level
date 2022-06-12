from itertools import product

n, m = map(int, input().split())

arr = [i for i in range(1, n+1)]

pro = product(arr, repeat=m)

for p in pro:
    for i in p:
        print(i, end=' ')
    print()