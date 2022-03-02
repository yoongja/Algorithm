M = int(input())
N = int(input())

is_prime = list(range(M,N+1))
real_is_prime = []
prime_sum = 0 

for i in is_prime:
    tf = True
    if i != 1:
        for j in range(2,i):
            if i%j == 0:
                tf = False
                break
        if tf == True:
            real_is_prime.append(i)
            prime_sum += i

if prime_sum == 0:
    print(-1)
else:
    print(prime_sum)
    print(min(real_is_prime))
    
