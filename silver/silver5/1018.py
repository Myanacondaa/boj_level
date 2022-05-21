n, m = map(int, input().split())
chess = []
for i in range(n):
    chess.append(list(map(str, input())))
result = []

for i in range(n-7):            # 세로를 (n-8+1)번 자를 수 있음
    for j in range(m-7):        # 가로를 (m-8+1)번 자를 수 있음
        idx1 = 0
        idx2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if chess[a][b] != 'W': idx1 += 1
                    if chess[a][b] != 'B': idx2 += 1
                else:
                    if chess[a][b] != 'B': idx1 += 1
                    if chess[a][b] != 'W': idx2 += 1
        result.append(idx1)
        result.append(idx2)

print(min(result))
