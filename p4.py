##A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

##Find the largest palindrome made from the product of two 3-digit numbers.

def pal(num):
    length = len(num)
    for i in range(int(length/2)):
        if num[i] != num[-i-1]:
            return(False)
    else:
        return(True) 

l1 = []
for i in range(9, -1, -1):
    for j in range(9, -1, -1):
        for k in range(9, -1, -1):
            for l in range(9, -1, -1):
                for m in range(9, -1, -1):
                    for n in range(9, -1, -1):
                        num = str((100*i + 10*j + k)*(100*l + 10*m + n))
                        ispal = pal(num)
                        if ispal:
                            l1.append(int(num))
                            


print(max(l1))
