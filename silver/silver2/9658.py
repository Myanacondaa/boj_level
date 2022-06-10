n = int(input())
dp = [0]*(n+5)      # SK가 지는 것을 0, 이기는 것을 1
dp[1], dp[2], dp[3], dp[4] = 0, 1, 0, 1

for i in range(5, n+1):
    if dp[i-1] and dp[i-3] and dp[i-4]:     # SK가 1, 3, 4개를 가져갔을 때 모두 지는 경우면
        dp[i] = 0
    else:       # 하나라도 이기는 경우가 나오면
        dp[i] = 1

print('SK' if dp[n] == 1 else "CY")
