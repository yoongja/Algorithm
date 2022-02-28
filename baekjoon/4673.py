natural_num = set(range(1,10001))
not_self_num = set()
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    not_self_num.add(i)

self_num = sorted(natural_num - not_self_num)
for i in self_num:
    print(i)
