# 나이트는 무조건 오른쪽으로만 이동, 위 아래는 자유

n, m = map(int, input().split())
if n == 1:      # 세로나 가로의 길이가 1이면 시작점만 방문 가능
    print(1)

elif n == 2:        # 세로가 2라면 2,3방법만 사용해야하므로 무조건 방문횟수가 4 이하여야 한다.
    print(min(4, (m+1)//2))
else:
    if m <= 6:      # 가로가 6 이하라면 1번, 4번만 이용하는게 최대이므로
        print(min(4, m))

    else:
        print(m-2)