sum100 = sum(i for i in range(1, 101))
sqsum100 = sum100*sum100

sumsq100 = sum(i**2 for i in range(1, 101))

print(sqsum100 - sumsq100)