n = int(input())
cnt = 0
level = []
for _ in range(n):
    level.append(int(input()))

for i in range(n-2, -1, -1):        # 뒤에서부터 0번째까지
    if level[i] >= level[i+1]:
        cnt += level[i] - level[i+1] + 1
        level[i] = level[i+1]-1

print(cnt)