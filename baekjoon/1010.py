# 도시를 동쪽과 서쪽으로 나눔
# 서쪽에는 N개, 동쪽에는 M개(N<=M)
# 다리 겹칠 수 없음, 다리 지을 수 있는 경우의 수

t = int(input())

for _ in range(t):
    dp = [[-1 for _ in range(30)] for _ in range(30)]
    _n, _m = map(int,input().split())
    for n in range(1, _n + 1):
        for m in range(1, _m + 1):
            if n == m:
                dp[n][m] = 1
                continue
            if n == 1:
                dp[n][m] = m
                continue
            if m > n:
                dp[n][m] = dp[n - 1][m - 1] + dp[n][m - 1]
    print(dp[_n][_m])