import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(x: int, y: int):
    if x < 0 or y < 0 or x >= h or y >= w or land[x][y] == 0:
        return

    land[x][y] = 0

    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)

    dfs(x - 1, y - 1)  # 왼쪽 위 대각선
    dfs(x + 1, y - 1)  # 왼쪽 아래 대각선
    dfs(x + 1, y + 1)  # 오른쪽 아래 대각선
    dfs(x - 1, y + 1)  # 오른쪽 위 대각선


if __name__ == "__main__":
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            exit(0)
        land = []
        for _ in range(h):
            land.append(list(map(int, input().split())))
        cnt = 0
        for i in range(h):
            for j in range(w):
                if land[i][j] == 1:
                    dfs(i, j)
                    cnt += 1

        print(cnt)
