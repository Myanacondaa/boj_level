from math import factorial
# 최단 경로 문제: 순열 이용
n, m, k = map(int, input().split())
if k == 0:
    print(int(factorial(n+m-2)/(factorial(n-1)*factorial(m-1))))

else:
    arr = [[j+i*m for j in range(1, m+1)] for i in range(n)]

    idx = [(i, j) for j in range(m) for i in range(n) if arr[i][j] == k]
    x, y = idx[0][0], idx[0][1]     # k의 인덱스
    # (0, 0) 부터 k의 인덱스까지의 최단 경로의 경우의 수
    res1 = int(factorial(x+y)/(factorial(x)*factorial(y)))
    n -= x
    m -= y
    if n == 1 or m == 1:
        print(res1)

    else:
        res2 = int(factorial(n+m-2)/(factorial(n-1)*factorial(m-1)))
        print(res1*res2)

