import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m, k = map(int, input().split())
graph = [[0]*(m+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1
cnt = 0


def dfs(x: int, y: int):
    global cnt
    if x < 0 or y < 0 or x > n or y > m or graph[x][y] == 0:
        return
    graph[x][y] = 0
    cnt += 1
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)


res = 1
for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] == 1:
            dfs(i, j)
            if res < cnt:
                res = cnt
            cnt = 0

print(res)