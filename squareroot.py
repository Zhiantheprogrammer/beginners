n=int(input("give a number"))
x=1
while (n<=0 or n>0):
    if x*x==n:
        print("the number ",n,"is a perfect square and the square root of",n,"is",x)
        break
    else:
        x=x+1 
        if x>=n:
             print("the number you gave is not a perfect square")
             break