n = int(input())

dp = [i for i in range(n+1)]        # 1^2 로 표현하는 식의 개수

for i in range(1, n+1):
    for j in range(i):
        if j**2 > i:
            break
        if dp[i] > dp[i - j**2]+1:      # 1을 더한 이유는 j**2도 포함해야 하므로 (+1개)
            dp[i] = dp[i - j**2]+1

print(dp[n])