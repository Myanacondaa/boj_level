from collections import deque
a, b = map(int, input().split())

res = -1

qu = deque([(a, 1)])

while qu:
    i, cnt = qu.popleft()
    if i == b:
        res = cnt
        break

    if i*2 <= b:
        qu.append((i*2, cnt+1))

    if int(str(i)+'1') <= b:
        qu.append((int(str(i)+'1'), cnt+1))

print(res)