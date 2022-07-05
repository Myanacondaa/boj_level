n = int(input())
counsel = [list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)
for i in range(n):
    if i + counsel[i][0] <= n:
        dp[i+counsel[i][0]] = max(dp[i+counsel[i][0]], dp[i]+counsel[i][1])
    dp[i+1] = max(dp[i+1], dp[i])
print(dp[n])