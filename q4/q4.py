import string
import time

start = time.time()


# Loop through all six-digit numbers
for i in range (100000,999999,1):
    
    # Extract first and last digits of the number
    first_digit=i//100000
    last_digit=i%10
    
    # Extract second and fifth digits of the number
    second_digit=i//10000
    second_digit=second_digit%10
    fifth_digit=i%100
    fifth_digit=fifth_digit//10 
    
    # Extract third and fourth digits of the number
    third_digit=i//1000
    third_digit=third_digit%10
    fourth_digit=i//100
    fourth_digit=fourth_digit%10
       
    # Check if the number is a palindrome
    if first_digit==last_digit and second_digit==fifth_digit and third_digit==fourth_digit:
        
        # Loop through all three-digit numbers
        for j in range (100,999,1):
            
            # Check if the number is divisible by the three-digit number
            remainder=i%j
            quotient=i//j
            if remainder==0 and quotient<=999:
                
                # Print the number and the factors
                print(i,"::",j,"*",quotient)

end = time.time()

print(end - start)