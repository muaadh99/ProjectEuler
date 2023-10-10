import time 

start = time.time()

numbers = [0]*1000000

highestlen=0
number2=0

def collatz_length(n, memo):
    if n < len(memo) and memo[n] != 0:
        return memo[n]
    
    if n == 1:
        return 1
    
    if n % 2 == 0:
        nehighestlent_n = n // 2
    else:
        nehighestlent_n = 3 * n + 1
    
    length = 1 + collatz_length(nehighestlent_n, memo)
    
    if n < len(memo):
        memo[n] = length

    return length

for i in range (1,1000001,1):
    k=0
    number=i
    chainlength = collatz_length(number, numbers)
    if chainlength > highestlen:
        highestlen = chainlength
        number2 = i
                        
print(number2)
print(highestlen)  

end = time.time()
print("time taken" , end - start)
        
    