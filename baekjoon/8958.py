N= int(input())

for i in range(N):
    OX = input()
    result = 0
    O = 1

    for i in OX:
        if i =="O":
            result += O
            O+=1
        else:
            O = 1
    print(result)


