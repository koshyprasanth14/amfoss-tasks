def cprime(num):
    if num<=1:
        return False
    for i in range (2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

n=int(input())

for j in range (2, n+1):
    if cprime(j):
        print(j, end=' ')


print ('')