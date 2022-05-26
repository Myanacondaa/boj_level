dp = [0] * 36
dp[0] = 1
dp[1] = 1
dp[2] = 2
n = int(input())
for i in range(3, n+1):
    tmp = 0
    if i % 2:           # 홀수이면
        for j in range(i//2):
            tmp += 2*dp[j]*dp[i-j-1]
        dp[i] = tmp + dp[i//2]**2   # 가운데 값까지 계산해서 더하기

    else:
        for j in range(i // 2):
            tmp += 2 * dp[j] * dp[i - j - 1]
        dp[i] = tmp

print(dp[n])
