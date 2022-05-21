n, k = map(int, input().split())    # 공, 바구니 개수
minimum = k*(k+1)//2
if minimum > n:
    print(-1)
elif (n - minimum) % k == 0:
    print(k-1)
else:
    print(k)

