n=str(input("give a name"))
l=0
for x in(n):
    m=0
    for y in(n):
        if x==y:
            m=m+1
            if m>=2:
                print("the letter",x,"is reapeted in the name you gave ")
                quit()
print("there is no letter reapeted in the name you gave")
