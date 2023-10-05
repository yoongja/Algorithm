def recur(y, x):
    if y == n - 1 and x == m - 1:
        return 1
    
    if dp[y][x] != -1: # 모든 지점에서 계산이 한번이라도 된다면, 재사용!
        return dp[y][x]
    
    route = 0
    for dy, dx in [[0,-1],[0,1],[1,0],[-1,0]]:
        ey = y + dy
        ex = x + dx
        # 만약 범위를 넘지않다면
        if 0 <= ey < n and 0 <= ex < m :
            # 이동한 값이 더 작다면
            if graph[ey][ex] < graph[y][x] :
                route += recur(ey,ex)

    dp[y][x] = route
    return dp[y][x]

n, m = map(int,input().split())

graph = [list(map(int,(input().split()))) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]

ans = recur(0,0)
print(ans)