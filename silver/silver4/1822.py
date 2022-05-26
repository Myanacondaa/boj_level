n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
if len(a-b) == 0:
    print(len(a-b))
else:
    print(len(a-b))

    for r in sorted(a-b):
        print(r, end=' ')