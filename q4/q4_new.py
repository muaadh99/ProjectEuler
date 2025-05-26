
def largest_pal( ):
    largest_palindrome = 0

    for i in range (999 , 100 , -1):
        for j in range(i, 100 , -1):
            product = i*j
            if palindrome_checker(product) and product > largest_palindrome:
                largest_palindrome = product

    print( "Largest Palindrome is : ", largest_palindrome)



def palindrome_checker(n):
    if str(n) == str(n)[::-1]:
        return True


largest_pal()