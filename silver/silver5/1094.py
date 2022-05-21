x = int(input())
stick = [64, 32, 16, 8, 4, 2, 1]
cnt = 0
result = 0
for s in stick:
    if x >= s:
        cnt += 1
        x -= s

    if x == 0:
        print(cnt)
        exit(0)

