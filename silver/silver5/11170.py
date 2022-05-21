t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = [str(i) for i in range(n, m+1)]
    sum_zero = 0
    for ele in result:
        sum_zero += ele.count('0')

    print(sum_zero)