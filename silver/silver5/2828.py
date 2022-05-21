n, m = map(int, input().split())
j = int(input())
pl = 1      # 왼쪽은 시작점인 1
pc = m      #  오른쪽은 바구니의 길이만큼 위치해 있음
cnt = 0
for _ in range(j):
    apple = int(input())

    if apple < pl:      # 사과가 바구니의 왼쪽에 있을 때
        cnt += pl - apple   # 바구니의 위치에서 사과가 떨어지는 위치의 차이만큼 이동
        pl = apple
        pc = apple + (m-1)

    elif apple > pc:       # 사과가 바구니의 오른쪽에 있을 때
        cnt += apple - pc
        pc = apple
        pl = apple - (m-1)


print(cnt)