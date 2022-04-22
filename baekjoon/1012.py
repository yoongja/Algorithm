from collections import deque

queue = deque()

dx = [-1,1,0,0] #상하좌우
dy = [0,0,-1,1]

def bfs(x,y):
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= m or ny <= -1 or ny >= n:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = 0 #방문처리하기
                queue.append((nx,ny))

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    arr = [[0]*n for _ in range(m)] 
    cnt = 0
    for i in range(k):
        x,y = map(int,input().split())
        arr[x][y] = 1 #배추가 심어져 있는 위치 1로 만들기

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)
