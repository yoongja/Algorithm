from collections import deque

n, m = map(int,input().split())  # n명의 학생들, m 은 키를 비교한 회수

# m개의 줄에는 키를 비교한 두 학생의 번호 a, b

# 각 노드에 연결된 간선 정보를 담기 위한 리스트
graph = [[] for _ in range(n + 1)]

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n + 1)

# 그래프 만들기 .. ? 간선넣기 ..?
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

# def topology_sort():
result = []
q = deque()

# 진입차수가 0인 노드를 큐에 넣음
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

# 큐가 빌때까지 다음의 과정 반복
while q:
    # 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
    for g in graph[now]:
        indegree[g] -= 1
        # 새롭게 진입차수 0이된 노드를 큐에 삽입
        if indegree[g] == 0:
            q.append(g)

print(*result)
