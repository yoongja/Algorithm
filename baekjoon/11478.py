string = input()

ans = set()

for i in range(len(string)):
	for j in range(i,len(string)):
		temp = string[i:j+1]
		ans.add(temp) #집합은 add임
print(len(ans))
'''
a = "abc"
print(a[0:1]) #마지막꺼는 출력안됨!
print(a[0:2])
'''
#print(diff_string)