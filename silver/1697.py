from collections import deque
MAX = 10**5


def bfs(n: int, k: int) -> None:
    queue = deque([n])
    dist = [0]*(MAX+1)  # 시간 초과 방지

    while queue:    # 큐가 비어있지 않을 때까지
        cur = queue.popleft()   # 현재 위치 인덱스에 대입

        if cur == k:    # 동생 위치와 같다면
            print(dist[cur])     # 현재 위치 인덱스에 해당하는 거리 출력
            return

        for nx in (cur-1, cur+1, cur*2):
            if 0 <= nx <= MAX and not dist[nx]:   # 범위 안에 있고 중복되지 않으면
                dist[nx] = dist[cur]+1  # 현재 위치 + 1
                queue.append(nx)    # 인덱스 추가


if __name__ == "__main__":
    N, K = map(int, input().split())
    bfs(N, K)
