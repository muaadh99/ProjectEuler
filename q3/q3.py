import math

# Take input from user
n = int(input("Input The Number:"))

# Print prime factors of the input number
print("Prime factors")

# Initialize loop variable
i = 1

# Loop through all numbers less than or equal to the square root of the input number
while(i <= math.sqrt(n)):
    k = 0

    # Check if the current number is a factor of the input number
    if (n % i == 0):
        j = 1

        # Count the number of factors of the current number
        while(j <= i):
            if (i % j == 0):
                k = k + 1
            j = j + 1

        # If the current number is prime, print it
        if(k == 2):
            print(i)

    # Increment loop variable
    i = i + 1