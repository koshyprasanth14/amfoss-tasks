t = int(input())
for i in range (t):
    num = int(input())
    z = []
    for fgh in range(num):
        if fgh%3 == 0 or fgh%5 == 0:
            z.append(fgh)

    print(sum(z))
    