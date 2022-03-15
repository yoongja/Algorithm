def dfs(graph,v,visited):

    visited[v] = True
    print(v,end=' ')

    for i in graph[v]:
        print(f'{i}현재 탐색할 부분')
        if not visited[i]:
            dfs(graph,i,visited) #깊이 우선 탐색이므로 인접노드의 인접노드를 계속 파고들어감 => 재귀 / 더이상 찾을게 없으면 함수호출했던 순서로 나오게 됨

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph,1,visited)
