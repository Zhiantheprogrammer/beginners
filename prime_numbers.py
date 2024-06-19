n=int(input("give number"))
y=n-1
x=2
while n>=0:
    if n%x==0:
        print ("number is not a prime number as it is divisible ",x )
        break
    else:
        x=x+1 
        if x>y:
            print("number is a prime number as it is only divisble by 1 and itself")
            break