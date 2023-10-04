import time

# Start the timer
start = time.time()

# Initialize the loop variable
num = 2*3*5*7*11*13*17*19

# Loop through all numbers greater than or equal to 2520
while (num >= 2520):
    count = 0
    factor = 1
    found = False
    
    # Check if the current number is divisible by all numbers from 1 to 20
    while (factor >= 1 and factor <= 20):
        if num % factor == 0:
            count = count + 1
        else:
            break

        factor = factor + 1
        
        # If the current number is divisible by all numbers from 1 to 20, print it
        if count == 20:
            print(num)
            found = True
            break
    if found:
        break
    
    # Increment the loop variable by 19
    num = num + 19

# End the timer
end = time.time()

# Print the time taken to execute the code
print(end - start)