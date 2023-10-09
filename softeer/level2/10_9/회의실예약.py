n, m  = map(int,input().split())
name = []
time_table = ["09","10","11","12","13","14","15","16","17","18"]
for i in range(n):
    name.append((input(),i))

# 18시는 존재하지 않음
time = [[0 for _ in range(9)] for _ in range(n)] # 회의실 예약가능 시각 9시간
for _ in range(m) : # 예약된 개수
    n, start, end = input().split() # n이 회의실 이름
    start, end = int(start) - 9, int(end) - 9
    for idx in range(len(name)): # name배열에서
        if name[idx][0] == n:
            for t in range(start, end):
                time[idx][t] = 1 #1로바꿈

ans = []
name.sort()
for im, Na in enumerate(name): # 회의실이름과, idx를 뽑음
    N, idx = Na
    print(f'Room {N}:')
    if 0 not in time[idx]: # 다 1로차있다면
        print("Not available")
    else:
        t = 0
        ans = []
        while t < 9:
            bol = False
            if time[idx][t] == 0: #비어있다면
                bol = True
                start = t
                for n_t in range(t,9):
                    if time[idx][n_t] == 1:
                        end = n_t # 하나적은수!
                        ans.append(f'{time_table[start]}-{time_table[end]}')
                        t = n_t
                        bol = False
                        break
                if bol == True:
                    ans.append(f'{time_table[start]}-18')
                    break
            else:
                t += 1
        print(f'{len(ans)} available:')
        for i in ans:
            print(i)
    if im != len(name)-1:
        print('-----') 
            