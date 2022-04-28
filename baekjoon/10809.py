s = input()
arr = [-1 for _ in range(26)]

for i in s:
    arr[ord(i)-97] = s.index(i)

print(*arr)