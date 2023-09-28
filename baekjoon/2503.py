# A가 정답으로 생각할 수 있는 모든 수를 넣어보기!

# B가 도전한 내용에 맞는지 확인하기!

n = int(input())

hint = [list(map(int,input().split())) for _ in range(4)]

# 100 ~ 999
for a in range(1,10):
    for b in range(10):
        for c in range(10):
            
            if ( a == b or b == c or c == a):
                continue

            # 숫자가 정해졌다면
            cnt = 0
            for arr in hint:
                number = arr[0] # hint
                ball = arr[1]
                strike = arr[2]

                # a,b,c 라는 숫자를
                # number하고 비교
                # 자리수가 같다면 strike올리고, 존재한다면 ball 올리고
                hun = number // 100
                ten = (number // 10) % 10
                il = number % 10

                ball_cnt = 0
                strike_cnt = 0

                if a == hun or b == ten or a == il:
                    ball_cnt += 1
                    if a == hun:
                        strike_cnt += 1
                if b == hun or b == ten or b == il:
                    ball_cnt += 1
                    if b == ten :
                        strike_cnt += 1
                if c == hun or c == ten or c == il:
                    ball_cnt += 1
                    if c == il :
                        strike_cnt += 1

                if ball == ball_cnt and strike == strike_cnt:
                    cnt += 1
print(cnt)