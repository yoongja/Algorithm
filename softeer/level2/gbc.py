n,m = map(int,input().split())

n_arr = []
m_arr = []

for _ in range(n):
    a, b = map(int,input().split())
    for _ in range(a):
        n_arr.append(b)

for _ in range(m):
    a, b = map(int,input().split())
    for _ in range(a):
        m_arr.append(b)

max = 0
for i in range(len(n_arr)):
    if max < m_arr[i] - n_arr[i]:
        max = m_arr[i] - n_arr[i]

print(max)
