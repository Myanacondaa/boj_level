from math import ceil, trunc
n = int(input())
# 두번 째 수를 x라고 할 때, less <= x <= more 계속해서 범위를 줄여 두번쨰 값 찾기
# 시작은 0 <= x <= n
# less와 more은 피보나치 수열처럼 감소함
more = n
less = 0
fibo = [[0, 0] for _ in range(30)]
fibo[0] = [0, 1]
fibo[1] = [n, 1]
i = 2    # 0부터 시작해서 위의 less와 more값을 할당 했으니 +2 증가

while less != more:
    fibo[i][0] = fibo[i - 1][0] + fibo[i - 2][0]
    fibo[i][1] = fibo[i - 1][1] + fibo[i - 2][1]

    if i % 2 == 0:    # less 값 할당
        less = ceil(fibo[i][0]/fibo[i][1])

    else:       # more 값 할당
        more = trunc(fibo[i][0]/fibo[i][1])

    i += 1


tmp = [-1]*20
tmp[0] = n
tmp[1] = more
result = [tmp[0], tmp[1]]
for i in range(2, len(tmp)):
    if tmp[i-2]-tmp[i-1] < 0:
        break
    tmp[i] = tmp[i-2]-tmp[i-1]
    result.append(tmp[i])


print(len(result))
for ele in result:
    if ele < 0:
        exit(0)
    print(ele, end=' ')

'''
12
4231 2615 1616 999 617 382 235 147 88 59 29 30 
'''