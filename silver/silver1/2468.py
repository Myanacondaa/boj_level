import sys
import copy
sys.setrecursionlimit(10**4)        # 백준의 재귀 호출은 최대 천번, 재귀 호출을 늘림
n = int(input())        # 행(열) 개수
area = []               # 지점 이차원 리스트
maximum = -1e9          # 최댓값
for _ in range(n):
    area.append(list(map(int, input().split())))


def drown_area(arr: list[list[int]], rain_height: int) -> int:
    # 물에 잠긴 지역은 0으로 표시
    for i in range(n):
        for j in range(n):
            if rain_height >= arr[i][j]:  # 비의 높이보다 작으면 잠김, 0으로 표기
                arr[i][j] = 0

    def dfs(x: int, y:int):
        if x < 0 or y < 0 or x >= n or y >= n or arr[x][y] == 0:
            # 범위에 벗어나거나 비에 잠긴 도시이면 종료
            return

        arr[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                dfs(i, j)
                cnt += 1
    return cnt


city = copy.deepcopy(area)      # drown_area 에서 area의 값이 변경됨.

for rain in range(min(min(area))-1, max(max(area))):
    # 비의 높이는 배열의 최솟값-1 ~ 최댓값-1이다.
    maximum = max(maximum, drown_area(area, rain))  # 지역을 의미하는 배열에 물에 잠긴 도시 표시
    area = copy.deepcopy(city)

print(maximum)
