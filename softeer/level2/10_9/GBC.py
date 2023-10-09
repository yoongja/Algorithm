n, m = map(int,input().split())


first_arr = [0] * 100
for _ in range(n):
    length, speed = map(int,input().split())
    for _ in range(length):
        first_arr.append(speed)

second_arr = [0] * 100
for _ in range(m):
    length, speed = map(int,input().split())
    for _ in range(length):
        second_arr.append(speed)

dp = []
for i in range(len(first_arr)):
    if first_arr[i] >= second_arr[i]:
        dp.append(0)
    else:
        dp.append(second_arr[i] - first_arr[i])


print(max(dp))