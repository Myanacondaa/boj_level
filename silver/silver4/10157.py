c, r = map(int, input().split())    # r행 c열
seat = int(input())
arr = [[0] * c for _ in range(r)]
num = 1
x, y = 0, 0

while num < c*r:
    while y-1 >= 0:     # 왼쪽 인덱스 범위를 벗어나지 않을때까지
        if arr[x][y-1] == 0:    # 왼쪽이 막히지 않았다면
            arr[x][y] = num
            num += 1
            y -= 1      # 왼쪽으로 이동
        else:
            break

    while x+1 < r:      # 아래 인덱스 범위를 벗어나지 않을때까지
        if arr[x+1][y] == 0: # 아래쪽이 막히지 않았다면
            arr[x][y] = num
            num += 1
            x += 1      # 아래로 이동
        else:
            break

    while y+1 < c:      # 오른쪽 인덱스 범위를 벗어나지 않을때까지
        if arr[x][y+1] == 0: # 오른쪽이 막히지 않았다면
            arr[x][y] = num
            num += 1
            y += 1
        else:
            break

    while x-1 >= 0:     # 위쪽 인덱스 범위를 벗어나지 않을때까지
        if arr[x-1][y] == 0:        # 위쪽이 막히지 않았다면
            arr[x][y] = num
            num += 1
            x -= 1
        else:
            break

for i in range(r):
    if 0 in arr[i]:             # 맨 마지막 값은 0이므로 0의 인덱스 찾기
        arr[i][arr[i].index(0)] = num       # 맨마지막 값 할당
        break

for i in range(r):
    for j in range(c):
        if seat == arr[i][j]:
            print(j+1, i+1)
            exit(0)

print(0)