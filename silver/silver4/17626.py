n = int(input())
dp = [0] * (n + 1)
dp[0], dp[1] = 0, 1

for i in range(2, n + 1):
    minimum = 500000
    j = 1
    while j ** 2 <= i:
        minimum = min(minimum, dp[i - (j ** 2)])
        j += 1
    dp[i] = minimum + 1

print(dp[n])