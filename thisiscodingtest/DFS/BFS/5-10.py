n,m = map(int,input().split()) #int로 넣어주기 위해 map 요소 사용
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False #주어진 범위 벗어나면 즉시 종료
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x , y - 1)
        dfs(x + 1, y)
        dfs(x , y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)

