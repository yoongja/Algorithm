H,M = map(int,input().split())
S = int(input())

h = 0
m = 0

h = (((M+S)//60) + H)%24
m = (M+S)%60

print(h,m)
