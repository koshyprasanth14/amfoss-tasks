def largest_prime_factor(number):
    i = 2  

    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i

    return number

t = int(input())
for ghi in range (t):
    number = int(input())

    result = largest_prime_factor(number)
    print(result)
