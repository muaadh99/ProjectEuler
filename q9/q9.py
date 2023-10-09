import time

start = time.time() # start the timer

# loop through numbers a from 1 to 999
for a in range (1,1000,1):
    x=a*a                              # calculate the square of a
    # loop through numbers b from a to 999
    for b in range (a,1000,1):
        y=b*b              
        c = 1000 - a - b               # calculate the value of c
        z=c*c                          # calculate the square of c
        if (x+y==z):                   # if a^2 + b^2 = c^2
            print(a*b*c)               # print the product of a, b, and c
            print(a,b,c)               # print the values of a, b, and c
            break                      # exit the inner loop

end = time.time() # stop the timer

print(end - start, "seconds") # print the time taken to execute the code