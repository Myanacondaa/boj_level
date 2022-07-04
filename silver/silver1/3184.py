import sys
sys.setrecursionlimit(10**5)
r, c = map(int, input().split())
fence = []
for _ in range(r):
    fence.append(list(map(str, input())))

sheep, wolf = 0, 0      # 섬을 파악할 때의 양과 늑대 수
cnt_sheep, cnt_wolf = 0, 0  # 총 양과 늑대의 수


def dfs(x: int, y: int):
    # 섬의 개수와 같은 문제
    # '#'가 아닌 곳을 섬으로 판단
    global sheep, wolf
    if x < 0 or y < 0 or x >= r or y >= c or fence[x][y] == '#':
        return
    if fence[x][y] == 'o':  # 섬이 o이면 양 +1
        sheep += 1

    elif fence[x][y] == 'v':    # 섬이 v이면 늑대 + 1
        wolf += 1

    fence[x][y] = '#'       # 섬이 아닌 곳(#)으로 바꾸기
    dfs(x, y-1)
    dfs(x, y+1)
    dfs(x-1, y)
    dfs(x+1, y)


for i in range(r):
    for j in range(c):
        if fence[i][j] != '#':
            dfs(i, j)
            if sheep > wolf:    # 양이 늑대보다 많으면 늑대는 사라지고, 양의 수만큼 증가
                cnt_sheep += sheep

            elif sheep <= wolf:  # 늑대가 양보다 많으면 양은 사라지고, 늑대의 수만큼 증가
                cnt_wolf += wolf
        sheep, wolf = 0, 0      # 섬으로 판단되는 양과 늑대 수 초기화

print(cnt_sheep, cnt_wolf)