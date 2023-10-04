import time

start = time.time() # start the timer

sum1=0 # initialize sum1 to 0
sum2=0 # initialize sum2 to 0

# loop through the numbers 1 to 100
for i in range (1,101,1):
    sum1 += i # add the current number to sum1
    sum2 += i**2 # add the square of the current number to sum2

difference =  (sum1**2) - sum2 # calculate the difference between the square of the sum and the sum of the squares
print(difference) # print the difference

end = time.time() # stop the timer
print(end - start) # print the time taken to execute the code