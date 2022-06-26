def sol(arr):
    for list in arr:
        if list.count(0) == 0 : #베영개 즉 모
            print('E')
        elif list.count(0) == 1 : #베한개 즉 도
            print('A')
        elif list.count(0) == 2 : #배두개 즉 개
            print('B')
        elif list.count(0) == 3: #배세개 즉 걸
            print('C')
        else: #베내개 즉 윷
            print("D")

arr = [list(map(int,input().split())) for _ in range(3)]
sol(arr)