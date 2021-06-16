#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


num = 600851475143

## iterate until all primes found 

## break if prime factor found

prime_factors = []
while num != 1:
    for i in range(2, num+1):
        if num % i == 0:
            num = int(num/i)
            prime_factors.append(i)
            print(num, i)
            break
    
print(i)