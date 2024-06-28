n=int(input("input a number"))
nn=int(input("input another number"))
x=1
while x>=0: 
    if(x%n==0) and (x%nn==0):
        print("lcm of",n,"and",nn,"is=",x)
        break
    else:
        x=x+1
