n = int(input())
dp =[[0]*3 for _ in range(n+1)]
for i in range(3):
    # [1][0]: 사자가 양 옆에 없을 때
    # [1][1]: 사자가 왼쪽에 있을 때
    # [1][2]: 사자가 오른쪽에 있을 때
    dp[1][i] = 1

for i in range(2, n+1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][0]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901

print(sum(dp[n]) % 9901)