
# Online Python - IDE, Editor, Compiler, Interpreter
n=(input("give a number"))
if (n.isnumeric()):
    n=int(n)
    x=0
    while n>0:
            m=int(n%10)
            n=int(n/10)
            x=(x+m)
       
        
    print(x)
else:
    print("please input a valid number")
