import math
import time

def count_divisors(n):
    divisors = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        # If i is a divisor, count it and its paired divisor (n // i)
        if n % i == 0:
            divisors += 1
            # Check if it's not a square root (to avoid double counting)
            if i != n // i:
                divisors += 1
    return divisors

start = time.time()

for i in range(100000):
    x = i * (i + 1) // 2
    if count_divisors(x) > 500:
        print(x)
        break

end = time.time() - start
print(end)
