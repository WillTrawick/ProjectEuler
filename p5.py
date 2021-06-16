#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def primefactor(num):
    primes = []
    while num != 1:
        for i in range(2, num+1):
           
            if num % i == 0:
                
                primes.append(i)
                num = int(num/i)
                break
    return(primes)


d = {}

for i in range(2, 21):
    d[i] = 0

for i in range(2, 21):
    factors = primefactor(i)
    unique = set(factors)
    for j in unique:
        count = factors.count(j)
        d[j] = max(d[j], count)


num = 1
for i in range(2, 21):
    num *= i**d[i]
print(num)