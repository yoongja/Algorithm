n = int(input())
stair = [int(input()) for _ in range(n)]

dp = [0 for _ in range(n)]

# dp에는 가장 큰 값을 저장한다
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0]+stair[2],stair[1]+stair[2])
for i in range(3,n):
    dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

print(max(dp))