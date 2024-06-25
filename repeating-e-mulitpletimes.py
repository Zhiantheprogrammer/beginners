n=str(input("give a name"))
x=0
m=0
for y in (n):
        if (y=="e"):
            x=x+1
            if x>=2:
                m=m+1
if m>=1:               
    print("letter e is reapeated",(m+1),"times")
else:             
    print("the letter e is not repeted")
