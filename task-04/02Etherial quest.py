n=int(input())
v1, v2, v3=0, 0, 0
for i in range (n):
    vector=list(map(int, input().split()))
    v1=v1+vector[0]
    v2=v2+vector[1]
    v3=v3+vector[2]

if (v1, v2, v3) == (0, 0, 0):
    print('YES')

else: 
    print('NO')