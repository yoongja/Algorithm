from collections import deque

def bfs(graph,start,visited):
    queue = deque([start]) #start를  queue에 포함한다
    visited[start] = True
    while queue:
        v = queue.popleft() #최하단을 꺼냄
        print(v,end='')

        for i in graph[v]: #방문하지 않은 인접리스트를 모두다 넣음
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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

visited = [False]*9 #0번째 인덱스를 없음으로 처리하므로 노드의 개수보다 하나많게 끔

bfs(graph,1,visited)