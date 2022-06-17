import sys
input = sys.stdin.readline


def reverse(x: int, y: int):
    for i in range(x, x+3):
        for j in range(y, y+3):
            arr[i][j] = 1 - arr[i][j]


n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
res = [list(map(int, input().strip())) for _ in range(n)]


cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if arr[i][j] != res[i][j]:
            reverse(i, j)
            cnt += 1

for i in range(n):
    for j in range(m):
        if arr[i][j] != res[i][j]:
            print(-1)
            exit(0)

print(cnt)