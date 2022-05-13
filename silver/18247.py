T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    if N <12 or M < 4: # L4열은 a=1이라고 할 때, (12,4)이므로 이보다 작으면 좌석은 존재하지 않는다
        print(-1)

    else:
        print(11*M + 4) # L앞에 K(11)까지는 11*M만큼 좌석이 있으므로