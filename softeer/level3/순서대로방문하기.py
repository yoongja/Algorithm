def dfs(now, destIdx):
    global cnt
    if now == must_visit[destIdx]:
        if destIdx == m - 1:
            cnt += 1
            return
        else:
            destIdx += 1
    y,x = now
    visited[y][x] = 1
    for dy, dx in [[0,-1],[0,1],[1,0],[-1,0]]:
        ey = y + dy
        ex = x + dx
        # 만약 범위를 넘지않는다면
        if 0 <= ey < n and 0 <= ex < n and visited[ey][ex] == 0 and graph[y][x] == 0:
            # 만약 같다면 depth를 올려보내자
            dfs([ey,ex],destIdx)
    visited[y][x] = 0
    return

# 시작점과 도착점을 모두 검색하고, 중간에 거쳐야 하는 것을 거치는 애들의 경우의 수만 남겨두기
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
must_visit = []
cnt = 0
for _ in range(m):
    a,b = map(int,input().split())
    must_visit.append([b-1,a-1])
visited = [[0 for _ in range(n)] for _ in range(n)]
dfs(must_visit[0],1)
print(cnt)
