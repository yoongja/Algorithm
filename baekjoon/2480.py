prize=0
m = 0
arr=list(map(int,input().split()))

if arr[0]==arr[1] and arr[1]==arr[2] and arr[2]==arr[0]: #3개 같은경우
    prize = 10000+(arr[0]*1000)

elif arr[0] != arr[1] and arr[0] != arr[2] and arr[1] != arr[2]: #모두 다른경우
    m=max(arr)
    prize = m*100

else:
    if arr[0]==arr[1]:
        prize = 1000+(arr[0]*100)
    elif arr[1]==arr[2]:
        prize = 1000+(arr[1]*100)
    elif arr[0]==arr[2]:
        prize = 1000+(arr[0]*100)


print(prize)
