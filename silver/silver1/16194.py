n = int(input())
INF = 10e5
p = [0] + list(map(int, input().split()))
dp = [INF for _ in range(n+1)]
dp[0] = 0
for i in range(n+1):
    for j in range(i+1):
        dp[i] = min(dp[i], dp[i-j] + p[j])

print(dp[n])
