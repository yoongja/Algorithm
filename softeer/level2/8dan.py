arr = list(map(int,input().split()))
if arr[0] == 1:
    result = "ascending"
    for idx, num in enumerate(arr):
        if idx == len(arr) - 1:
            print(result)
            break
        if num + 1 != arr[idx + 1]:
            result = "mixed"
elif arr[0] == 8:
    result = "descending"
    for idx,num in enumerate(arr):
        if idx == len(arr) - 1:
            print(result)
            break
        if num - 1 != arr[idx + 1]:
            result = "mixed"
else:
    print("mixed")
