import string
for i in range (100000,999999,1):
    x=i//100000
    y=i%10
    
    l=i//10000
    m=l%10
    k=i%100
    h=k//10 
    
    a=i//1000
    b=a%10
    c=i//100
    d=c%10
       
    if x==y and m==h and b==d:
        for h in range (100,999,1):
            w=i%h
            s=i//h
            if w==0 and s<=999:
                print(i,"::",h,"*",s)
                
                
