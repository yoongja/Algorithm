N= int(input())
people = []
cnt = 1

for i in range(N):
    x,y  = map(int,input().split(' '))
    people.append((x,y)) # list에 tuple추가

for i in people: #큰범주에서의 비교대상
    grade = 1#자신보다 큰애를 만났을 경우에만 올라
    for j in people: #안에서 세부적인 비교대상감
        if (i[0]!=j[0]) | (i[1]!=j[1]): #같은 사람 방지
            if (i[0]<j[0]) & (i[1]<j[1]):
                grade +=1
    print(grade)
        
