from collections import deque
n = int(input())
qu = deque()
qu.append([n])
res = []
while qu:
    x = qu.popleft()
    num = x[0]
    if num == 1:
        res = x
        break

    if num % 3 == 0:
        qu.append([num//3] + x)

    if num % 2 == 0:
        qu.append([num//2] + x)

    qu.append([num-1] + x)


print(len(res)-1)
print(*(reversed(res)))