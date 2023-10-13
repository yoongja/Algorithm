# 계단은 한 번에 한 계단 또는 두 계단 씩
# 연속된 세 개의 계단을 모두 밟아서는 안됨, 시작점은 계단에 포함 x
# 마지막 도착 계단 반드시 밟아야 한다.
# 얻을 수 있는 총 점수의 최댓값
    
import sys

input = sys.stdin.readline

n = int(input()) # 계단의 개수
stair = [int(input()) for _ in range(n)] # 각 계단에 쓰여 있는 점수
dp = [0 for _ in range(n)] # dp테이블에 저장한것을 바탕으로 확인 ..?

# 첫 번째 계단
dp[0] = stair[0]
# 두 번째 계단
dp[1] = stair[0] + stair[1]
# 세 번째 계단 -> stair[1] + stair[2] or stair[0] + stair[2]
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i],dp[i-2] + stair[i])

print(dp)