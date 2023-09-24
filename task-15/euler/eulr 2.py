def fibonnaci(n):
    aadi = []
    z=[]
    aadi.append(1)
    aadi.append(2)
    third = 0

    while third < n :
        
            first = aadi[-2]
            second = aadi[-1]
            third = first + second

            if third <= n:
                aadi.append(third)

    for j in aadi:
        if j % 2 == 0:
            z.append(j)
    
    print(sum(z))


t = int(input())
for fghj in range (t):
    n = int(input())
    fibonnaci(n)