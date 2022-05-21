t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    print(sorted(arr, reverse=True)[2])