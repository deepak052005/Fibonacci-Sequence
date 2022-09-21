n= int(input ("no of values: "))
x=0
y=1
if n<=0:
    print ("invalid input")
elif n==1:
    print(x)
else:
    print(x)
    print(y)
    for i in range (2,n):
                        c=x+y
                        x=y
                        y=c
                        print (c)
    
