n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)

arr.sort(reverse=False)
for i in range(len(arr)):
    print(arr[i])