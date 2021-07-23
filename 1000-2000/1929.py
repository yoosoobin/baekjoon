import math

def isPrime(num):
    if num == 1:
        return False
    elif num in (2,3):
        return True
    else:
        n = int(math.sqrt(num))

        for i in range(2,n+1):
            if num%i ==0:
                return False
        return True

m,n = map(int,input().split())

for i in range(m,n+1):
    if isPrime(i):
        print(i)



