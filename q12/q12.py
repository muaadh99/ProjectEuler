import math
import time

start = time.time()

for i in range (0,100000,1):
    k=0
    x=(i*(i+1)//2)
    for j in range (1,int(math.sqrt(x))+1,1):
        if x%j==0:
            k=k+1

    if k>=250:                                   #x*y , likewise there are two factors. So twice the k value is the number of factors
        print(x)
        break

end = time.time() - start
print(end)