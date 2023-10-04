import math
n=int(input("Input The Number:"))
print("Prime factors")
i=1
while(i<=math.sqrt(n)):
    k=0
    if (n%i == 0):
        j=1
        while(j<=i):
            if (i%j == 0):
                k=k+1
            j=j+1
        if(k==2):
            print(i)
    i=i+1
            


        
                                    

