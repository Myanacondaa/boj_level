n, m = map(int, input().split())
num = int(input())
row = [0]        # 행 리스트
col = [0]        # 열 리스트
for _ in range(num):
    i, j = map(int, input().split())
    if i == 0:      # 가로면 행 리스트에 추가
        row.append(j)
    else:           # 세로면 열 리스트에 추가
        col.append(j)

row.append(m)
col.append(n)

row.sort()
col.sort()

max_row, max_col = 0, 0

for i in range(1, len(row)):
    if max_row < row[i] - row[i-1]:
        max_row = row[i] - row[i-1]

for i in range(1, len(col)):
    if max_col < col[i] - col[i-1]:
        max_col = col[i] - col[i-1]

print(max_row * max_col)
