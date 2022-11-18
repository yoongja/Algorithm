n = int(input())
arr = [1,1]

for i in range(2,90):
	arr.append(arr[i-1] + arr[i-2])

print(arr[n-1])