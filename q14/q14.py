import time 

start = time.time()                          # start the timer

numbers = [0]*1000000                        # initialize a list of 1000000 zeros to store the length of Collatz chains

highestlen=0                                 # initialize the highest length to 0
number2=0                                    # initialize the number with the highest length to 0

# function to calculate the length of a Collatz chain for a given number
def collatz_length(n, memo):
    if n < len(memo) and memo[n] != 0:       # if the length of the chain for the current number is already stored in the memo list
        return memo[n]                       # return the length of the chain from the memo list
    
    if n == 1:                               # if the current number is 1
        return 1                             # return 1 since the chain has ended
    
    if n % 2 == 0:                           # if the current number is even
        next_num = n // 2                    # calculate the next number in the chain
    else:                                    # if the current number is odd
        next_num = 3 * n + 1                 # calculate the next number in the chain
    
    length = 1 + collatz_length(next_num, memo) # calculate the length of the chain for the next number and add 1
    
    if n < len(memo):                        # if the current number is less than the length of the memo list
        memo[n] = length                     # store the length of the chain in the memo list at the current number index

    return length                            # return the length of the chain

# loop through numbers from 1 to 1000000
for i in range (1,1000001,1):
    k=0                                      # initialize the factor counter to 0
    number=i # set the current number to i
    chainlength = collatz_length(number, numbers) # calculate the length of the Collatz chain for the current number
    if chainlength > highestlen:             # if the length of the chain is greater than the current highest length
        highestlen = chainlength             # update the highest length with the new length
        number2 = i                          # update the number with the highest length with the new number
                
print(number2)                               # print the number with the highest length of the Collatz chain
print(highestlen)                            # print the length of the Collatz chain for the number with the highest length

end = time.time()                            # stop the timer
print("time taken" , end - start)            # print the time taken to execute the code