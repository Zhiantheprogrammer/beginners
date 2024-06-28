y=(input("untill wich multiplication table would you like"))
if (y.isnumeric()):
    y=int(y)
    n=1
    while n<=y:
        print("this is for multiplication table of",n)
        for x in range (1,11):
            m=x*n
            print(n," * ",x," = ",m)
        n=n+1
else:
    quit(print("please give a number",y,"is not an number"))
