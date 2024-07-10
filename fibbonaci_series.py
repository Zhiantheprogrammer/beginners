m=(input("untill wich fibonachi series do you want"))
try:
    m=int(m)
except:
    print("please give a valid number")
    quit()
print("1")
print("1")
a=1 
b=1 
for x in range(m):
    
    c=b+a 
    a=b 
    b=c
    
    print(c)
