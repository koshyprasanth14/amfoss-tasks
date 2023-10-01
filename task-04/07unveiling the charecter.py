
t = int(input())

for i in range (t):
    s=input()
    amfoss = 'amfoss'
    wrong = 0
    m = 0
    
    for m in range(6):
        if s[m] != amfoss[m]:
            wrong +=1
    
    print(wrong)
