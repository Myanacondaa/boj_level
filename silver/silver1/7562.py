from collections import deque


def move_knight(n: int, kn: list[int], d: list[int]) -> int:
    # 나이트는 총 8가지 방향으로 움직일 수 있고, 각각
    # 왼쪽 위: (-2, -1), 오른쪽 위: (-2, 1), 왼쪽 위옆: (-1, -2), 오른쪽 위옆: (-1, 2)
    # 왼쪽 아래옆: (1, -1), 오른쪽 아래옆: (1, 2), 왼쪽 아래: (2, -1), 오른쪽 아래: (2, 1)
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    dist = [[0] * n for _ in range(n)]      # n*n 크기의 체스판 생성
    dist[kn[0]][kn[1]] = 1                  # 현재 위치를 1로 표기
    queue = deque()
    queue.append([kn[0], kn[1]])            # 큐에 현재 위치 삽입
    while queue:
        x, y = queue.popleft()
        if x == d[0] and y == d[1]:         # 도착지의 x좌표와 y죄표가 같으면 종료
            return dist[x][y] - 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n or dist[nx][ny] != 0:
                # 범위를 벗어나거나 0이 아니면 컨티뉴
                continue

            queue.append([nx, ny])
            dist[nx][ny] = dist[x][y] + 1


t = int(input())
for _ in range(t):
    I = int(input())
    knight = list(map(int, input().split()))
    destination = list(map(int, input().split()))
    print(move_knight(I, knight, destination))

