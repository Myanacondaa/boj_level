import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
max_paint = 0
tmp = 0


def dfs(x: int, y: int):
    global tmp
    if x < 0 or y < 0 or x > n-1 or y > m-1 or paper[x][y] == 0:
        return

    tmp += 1
    paper[x][y] = 0

    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)


for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            dfs(i, j)
            cnt += 1
            if max_paint < tmp:
                max_paint = tmp

        tmp = 0

print(cnt)
print(max_paint)