import sys

sys.setrecursionlimit(10000)

def recur(y,x):
    if dp[y][x] != 0: # 이미 방문했다면 
        return dp[y][x]

    # 상,하,좌,우
    for dy,dx in [[-1,0],[1,0],[0,-1],[0,1]]:
        ey = y + dy
        ex = x + dx
        # 만약 범위를 넘지않다면
        if 0 <= ey < n and 0 <= ex < n :
            # 이동한 값이 더 크다면
            if graph[y][x] < graph[ey][ex]:
                dp[y][x] = max(dp[y][x], recur(ey,ex) + 1)
    return dp[y][x]
        
n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)] # n * n 짜리 dp생성, 1,1부터 시작

# 모든 좌표에서 돌도록 완전탐색 시키기!
for y in range(n):
    for x in range(n):
        recur(y,x)

print(max(map(max,dp)) + 1)
