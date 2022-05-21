dic = dict()
board = []
for i in range(5):
    board.append(list(map(int, input().split())))
    for j in range(5):
        dic[board[i][j]] = (i, j)       # 빙고판의 숫자를 키로, 위치를 값으로 하는 딕셔너리

call_num = []
for _ in range(5):
    call_num.append(list(map(int, input().split())))

check = [[0]*5 for _ in range(5)]       # check 5*5 이차원 리스트
bingo = 0
cnt = 0
for i in range(5):
    for j in range(5):
        tmp = call_num[i][j]
        x = dic[tmp][0]
        y = dic[tmp][1]
        check[x][y] = 1     # 해당하는 숫자의 빙고판의 인덱스에 체크
        cnt += 1
        if sum(check[x]) == 5:      # check 리스트 가로의 합이 5
            bingo += 1
        if sum([check[k][y] for k in range(5)]) == 5:   # check 리스트 세로의 합이 5
            bingo += 1
        if x == y:
            if sum([check[k][k] for k in range(5)]) == 5:   # 왼쪽 대각선의 합이 5
                bingo += 1
        if x+y == 4:
            if sum([check[k][4-k] for k in range(5)]) == 5:  # 오른쪽 대각선의 합이 5
                bingo += 1

        if bingo >= 3:
            print(cnt)
            exit(0)





