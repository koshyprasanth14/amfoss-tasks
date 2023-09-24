def palindrome(input_number):
    z = []
    for i in range(1000, 99, -1):
        for j in range (1000, 99, -1):
            num = i * j 
            if str(num) == str(num)[ ::-1]:
                if num <= input_number:
                    z.append(num)
                    
                    

    if z:
        print(max(z))
    else:
        print(0)


t = int(input())
for fgh in range (t):
    input_number = int(input())
    palindrome(input_number)