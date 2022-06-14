n = int(input()) # 삼각형 크기
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

if n ==1: # 개수가 한 개이면
    print(tri[0][0])

else:
    tri[1][0] += tri[0][0] # 2행 1열 값 계산
    tri[1][1] += tri[0][0] # 2행 2열 값 계산

    for i in range(2, n):
        tri[i][0] += tri[i - 1][0] # 맨 앞 값은 바로 위 행의 맨 앞 값만 더함
        tri[i][-1] += tri[i - 1][-1] # 맨 뒤 값은 바로 위 행의 맨 뒤 값만 더함
        for j in range(1, len(tri[i])-1):
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

    print(max(tri[-1]))
