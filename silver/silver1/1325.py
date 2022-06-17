from collections import deque
import sys
input = sys.stdin.readline


def bfs(start: int) -> int:
    cnt = 1
    qu = deque([start])
    visit = [False for _ in range(n+1)]
    visit[start] = True

    while qu:
        cur = qu.popleft()
        for nx in trust[cur]:
            if not visit[nx]:
                visit[nx] = True
                cnt += 1
                qu.append(nx)

    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    trust = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        trust[b].append(a)

    max_cnt = 1
    res = []

    for i in range(1, n+1):
        cnt = bfs(i)
        if cnt > max_cnt:
            max_cnt = cnt
            res.clear()
            res.append(i)

        elif cnt == max_cnt:
            res.append(i)

    print(*res)