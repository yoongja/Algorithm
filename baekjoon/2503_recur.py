import sys

#python은 1000번돌면 재귀 종료돼서 늘려줌
# 메모리 -> 31492 KB
sys.setrecursionlimit(9999) 

def checker(hint, number):
    num_hun = number // 100
    num_ten = (number // 10) % 10
    num_il = number % 10

    if num_hun == 0 or num_ten == 0 or num_il == 0:
        return False
    if num_hun == num_ten or num_ten == num_il or num_il == num_hun:
        return False

    cnt_strike, cnt_ball = 0, 0
    hint_num, hint_strike, hint_ball = hint[0], hint[1], hint[2]
    hint_hun = hint_num // 100
    hint_ten = (hint_num // 10) % 10
    hint_il = hint_num % 10
    

    # strike 계산기
    if hint_hun == num_hun :
        cnt_strike += 1
    if hint_ten == num_ten :
        cnt_strike += 1
    if hint_il == num_il :
        cnt_strike += 1
    
    # ball 계산기
    if num_hun == hint_ten or num_hun == hint_il :
        cnt_ball += 1
    if num_ten == hint_hun or num_ten == hint_il :
        cnt_ball += 1
    if num_il == hint_ten or num_il == hint_hun :
        cnt_ball += 1
    
    if hint_strike == cnt_strike and hint_ball == cnt_ball :
        return True
    return False


def recur(hint_idx, number):
    global answer
    if hint_idx == n:
        answer += 1
        recur(0,number + 1)
        return

    if number == 1000:
        return

    # 만약에 힌트에 통과했다면
    # 스트라이크 카운트랑 볼 카운트가 동일하다면 
    if checker(hint[hint_idx],number):
        recur(hint_idx + 1, number)
    else:
        # 힌트에 통과하지 않았다면
        # 힌트를 다시 0부터
        recur(0, number + 1)

n = int(input())
hint = [list(map(int,input().split())) for _ in range(n)]
answer = 0
recur(0, 100) # 숫자 100부터 999숫자, 3가지 숫자는 1~9까지 모두 다른 숫자여야함
print(answer)