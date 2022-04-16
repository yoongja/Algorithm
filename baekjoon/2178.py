from collections import deque

queue = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input())))

def bfs(x,y):
    queue.append((x,y))
    while(queue):
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m :
                continue
            if arr[nx][ny] == 0 :
                continue
            if arr[nx][ny] == 1 :
                queue.append((nx,ny))
                arr[nx][ny] = arr[x][y] + 1
    return arr[n-1][m-1]


print(bfs(0,0))