arr = []
for i in range(9):
    N = int(input())
    arr.append(N)

Max = max(arr)
print(Max)
print(arr.index(Max)+1)
    
