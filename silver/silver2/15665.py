from itertools import product

n, m = map(int, input().split())

arr = list(map(int, input().split()))

for p in sorted(set(product(arr, repeat= m))):
    for j in p:
        print(j, end=' ')
    print()
