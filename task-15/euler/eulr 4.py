t = int(input())
for sdug in range (t):
    n = int(input())
    z = []
    for i in range (n-1, 101101 -1, -1):
        if str(i) == str(i)[::-1]:
            for j in range(100,1000):
                if i%j==0:
                    k = i//j
                    if k <= 999:
                        z.append(i)
                        break

        if len(z) == 1:
            break
    print(max(z))
