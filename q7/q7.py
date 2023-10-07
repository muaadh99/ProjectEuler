import time

start_time = time.time()                # start the timer

def nth_prime(n):
    prime_counter = 2                   # initialize the prime counter to 2 since 2 is the first prime number
    for num in range (3, n**2, 2):      # loop through odd numbers starting from 3
        divisor = 1                     # initialize the divisor to 1
        while divisor * divisor < num:  # loop through divisors up to the square root of the current number
            divisor += 2                # increment the divisor by 2 since even numbers are not prime
            if num % divisor == 0:      # if the current number is divisible by the divisor, it is not prime
                break                   # exit the loop
        else:                           # if the loop completes without finding a divisor, the current number is prime
            prime_counter += 1          # increment the prime counter
        if prime_counter == n:          # if we have found the nth prime number
            return num                  # return the current number
                
print(nth_prime(10001))                 # print the 10001st prime number

end_time = time.time()                  # stop the timer

print(end_time - start_time, "seconds") # print the time taken to execute the code