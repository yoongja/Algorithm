arr = list(input())
sol = []
cnt = 0

for what in arr:
    if 'A' <= what <= 'Z':
        sol.append(what)
    else:
        cnt += int(what)

sol.sort()
print(''.join(sol) + str(cnt))