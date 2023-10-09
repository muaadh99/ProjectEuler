import time

# function to generate primes using the Sieve of Eratosthenes algorithm
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)                                 # initialize a boolean list of size limit+1 with all values set to True
    sieve[0], sieve[1] = False, False                            # set the first two values to False since they are not prime
    for i in range(2, int(limit**0.5) + 1):                      # loop through numbers from 2 to the square root of limit
        if sieve[i]:                                             # if the current number is prime
            for j in range(i*i, limit + 1, i):                   # loop through multiples of the current number starting from its square
                sieve[j] = False                                 # mark the multiples as not prime
    return [i for i, val in enumerate(sieve) if val]             # return a list of all prime numbers up to limit

start = time.time() # start the timer

limit = 2000000                                                  # set the limit to 2 million
primes = sieve_of_eratosthenes(limit)                            # generate a list of all prime numbers up to the limit
sum_of_primes = sum(primes)                                      # calculate the sum of all prime numbers

end = time.time() - start                                        # stop the timer and calculate the time taken

print("Sum of primes:", sum_of_primes)                           # print the sum of all prime numbers
print("Time Taken:", end, "s")                                   # print the time taken to execute the code