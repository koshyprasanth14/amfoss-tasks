import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

def find_lcm(numbers):
    
    result = numbers[0]

    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    
    print(result)


t = int(input())
for i in range (t):
    num = int(input())
    numbers =[]
    for dfg in range (1, num +1):
        numbers.append(dfg)

    find_lcm(numbers)
