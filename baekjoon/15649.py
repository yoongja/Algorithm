n,m = map(int,input().split())

#백트래킹 = 절대 안되는 상황을 정의 !,재귀로 구현하며 조건이 맞지 않으면 종료,dfs 기반
arr = []

def dfs():
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return

    for i in range(1,n+1):
        if i not in arr: 
            arr.append(i)
            dfs()
            arr.pop()

dfs()
