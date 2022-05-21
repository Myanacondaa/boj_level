s = input()
n = int(input())
cnt = 0
for i in range(n):
    ring = input()
    if s in ring+ring:
        cnt += 1

print(cnt)