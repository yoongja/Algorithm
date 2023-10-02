def recur(idx, weight):
    global answer
    if weight > B : # 가방 무게보다 커진다면 그만 찾아도 돼!
        return -999999
    if idx == N : # 인덱스가 마지막까지 도달한다면
        return 0
    if dp[idx][weight] != -1: # 이미 저장되어 있다면 , 돌려주어서 필요없는 연산이 반복되지 않도록함!
        return dp[idx][weight]

    dp[idx][weight] = max(recur( idx + 1, weight + items[idx][0]) + items[idx][1], recur(idx + 1, weight + items[idx][0]))
    return dp[idx][weight]

N, B = map(int,input().split())
items = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1 for _ in range(100_001)] for _ in range(N)]
recur(0,0)
print(dp)