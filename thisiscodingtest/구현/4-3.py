from operator import index


N = 8
X,Y = input().split()

arr = ['a','b','c','d','e','f','g','h']
X = arr.index(X) #int(ord(X))-int(ord('a')) ord() returns an integer representing the unicode character
Y = int(Y)-1
posi = [(-2,1),(-2,-1),(2,1),(2,-1),(-1,2),(1,2),(-1,-2),(1,-2)] #이동가능한 8가지 방향수

cnt = 0 

for i in posi:
    if X+i[0]<0 or Y+i[1]<0 or X+i[0]>N or Y+i[1]>N:
        continue
    cnt +=1 

print(cnt)
