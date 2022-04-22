from collections import deque

m,n,h = map(int,input().split())
queue = deque()

arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1 :
                queue.append((i,j,k)) #익은 토마토 넣어주기

dx = [0,0,-1,1,0,0] #위,아래,왼,오,앞,뒤
dy = [0,0,0,0,-1,1]
dz = [1,-1,0,0,0,0]

def dfs():
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m or nz <= -1 or nz>=h:
                continue
            if arr[nx][ny][nz] == -1 :
                continue
            if arr[nx][ny][nz] == 0 :
                queue.append((nx,ny,nz))
                arr[nx][ny][nz] = arr[x][y][z] + 1

    result = max(map(max,map(max,arr))) - 1 

    br = False
    tr = False
    
    for row in arr :
        for col in row :
            for hei in col :
                if col == 0:
                    result = -1
                    br = True #이중for문 빠져나오기
                    tr = True
                    break
            if br == True:
                break
        if tr == True:
            break
       
    return result
    

print(dfs())
