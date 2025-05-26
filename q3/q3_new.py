import math

def prime_factors(n):
    prime_facts = []
    while n % 2 == 0:
        if 2 not in prime_facts:
            print(2)
            prime_facts.append(2)

        n = n//2

    # n must be odd at this point
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n%i == 0 :
            if i not in prime_facts:
                print(i)
                prime_facts.append(i)
            n = n//i

    
    if n > 2:
        prime_facts.append(n)
        print(n)


n = int(input("input your number : "))

print("prime factors")
prime_factors(n)