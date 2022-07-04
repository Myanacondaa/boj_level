import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append([home[0], home[1]])
    while q:
        x, y = q.popleft()
        if abs(x - fest[0]) + abs(y-fest[1]) <= 1000:
            # 노드 간 거리가 1000미터를 넘으면 안 됨: 50미터당 맥주 1개, 총 맥주 20개
            print('happy')
            return

        for i in range(n):
            if not visited[i]:      # 편의점을 방문하지 않았다면
                new_x, new_y = store[i] # 편의점 좌표
                if abs(x - new_x) + abs(y - new_y) <= 1000:
                    q.append([new_x, new_y])
                    visited[i] = 1

    print('sad')
    return


t = int(input())        # 테스트 케이스
for _ in range(t):
    n = int(input())        # 편의점 개수
    home = list(map(int, input().split()))     # 상근이의 집 좌표
    store = []      # 편의점 좌표
    for _ in range(n):      # 편의점 좌표 입력
        a, b = map(int, input().split())
        store.append([a, b])

    fest = list(map(int, input().split()))      # 페스티벌 좌표
    visited = [0 for i in range(n + 1)]  # home 제외
    bfs()