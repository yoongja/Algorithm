n, k = map(int,input().split()) # 학생 수, 구간 수

student_score = list(map(int,input().split())) # 학생의 성적
arr = [list(map(int,input().split())) for _ in range(k)] # 구간이 주어짐
# 누적합 dp테이블 만들어서 하기
dp = [0 for _ in range(n)]
dp[0] = student_score[0]
for i in range(1,n):
    dp[i] = student_score[i] + dp[i - 1]

for a,b in arr:
    if a == 1:
        sum = dp[b - 1]
    else:
        sum = dp[b - 1] - dp[a - 2]
    sum = sum / (abs(b-a) + 1)
    print(f'{round(sum,2):.2f}')
