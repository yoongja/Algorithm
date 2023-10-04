n = int(input())
dp = [-1 for _ in range(1001)]

for i in range(1,n + 1):
    if i == 1:
        dp[1] = 1
        continue
    if i == 2:
        dp[2] = 2
        continue
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)