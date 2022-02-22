N = int(input())
arr = list(map(int,input().split()))

Max = max(arr)
Sum=0


for i in arr:
    Sum += i/Max*100

avg = Sum/N
print(avg)
