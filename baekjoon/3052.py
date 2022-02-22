
arr2= []

for i in range(10):
    N= int(input())
    if N%42 not in arr2:
        arr2.append(N%42)
print(len(arr2))
