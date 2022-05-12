n,m = map(int,input().split())

arr = [] #숫자를 담아놓을 배열

def dfs(start):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(start,n+1):

        arr.append(i)
        dfs(i+1) #바로 전 노드보다 현재 노드의 수가 커야하는 조건을 추가하기
        arr.pop() 

dfs(1)
