from collections import deque


def bfs(x, y, d):
    global cnt
    q = deque()
    q.append((x,y))
    cnt = 1
    visited[x][y] = 1 # 처음 위치
    while q:
        nx, ny = q.popleft()
        # 현재 칸이 아직 청소되지 않았으면, 일단 현재 칸을 청소
        
        # 현재 칸의 주변 4칸 중 
        flag = 0
        for _ in range(4):
            d = (d + 3) % 4
            ex = dx[d] + nx
            ey = dy[d] + ny
            if 0 <= ex < n and 0 <= ey < m : # 범위를 벗어나지 않을경우
                # 4칸중 청소되지 않은 빈칸 있다면
                if visited[ex][ey] == 0 and graph[ex][ey] == 0:
                    visited[ex][ey] = 1
                    q.append((ex,ey)) # 이미 전진까지 함
                    flag = 1
                    cnt += 1
                    break # 한 칸 청소하고 멈춤
        if flag == 0: # 4칸중 청소되지 않은 빈칸없는 경우
            ex = nx - dx[d] # 후진
            ey = ny - dy[d]
            if graph[ex][ey] == 0: # 돌아갈 수 있다면
                q.append((ex,ey))
            else: # 돌아갈 수 없다면
                break

n, m = map(int,input().split())
r, c, d = map(int,input().split()) # 처음 로봇 청소기가 있는 칸의 좌표와, 로봇 청소기 바라보는 방향

graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1,0,1,0] # 북동남서
dy = [0,1,0,-1]
cnt = 0
bfs(r -1, c - 1, d)
print(cnt)
