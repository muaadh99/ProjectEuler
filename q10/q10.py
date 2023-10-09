import math
import time
start=time.time()

sum1=2

for i in range (3,2000000,2):
    k=0
    for n in range (3,int(math.sqrt(i))+1,2):
        if i%n==0:
            break 
    else:
        prime=i
        sum1 +=i 
         
end=time.time()-start
                        
print("Sum",sum1)
print("Prime number",prime) 
print("Time Taken",end," s")
