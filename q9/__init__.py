import time

start = time.time()

for a in range (1,1000,1):
    x=a*a
    for b in range (a,1000,1):
        y=b*b
        for c in range (b,1000,1):
            z=c*c
            if (x+y==z and a+b+c==1000):
                print(a*b*c)
                print(a,b,c)
                break

end = time.time()

print(end - start, "seconds")
                