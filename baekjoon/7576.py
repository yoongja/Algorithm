from collections import deque

m,n = map(int,input().split())
queue = deque()

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 :
            queue.append((i,j)) #익은 토마토 넣어주기

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if arr[nx][ny] == -1 :
                continue
            if arr[nx][ny] == 0 :
                queue.append((nx,ny))
                arr[nx][ny] = arr[x][y] + 1

    result = max(map(max,arr)) - 1 

    br = False
    
    for row in arr :
        for col in row :
            if col == 0:
                result = -1
                br = True
                break
        if br == True:
            break
       
    return result
    

print(dfs())


