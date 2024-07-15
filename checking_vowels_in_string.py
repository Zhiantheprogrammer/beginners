a=str(input("please give a string"))
b=["a","e","i","o","u"]
d=0
s=""
c=len(b)
for x in(a):
    for y in range(c):
        if b[y]==x:
            d=d+1
            s=s+b[y]
            print(s)
if d>1:
    print("the vowels",s,"are there in the string you input")
    quit()
if d==1:
    print("the vowel",s,"is there in the string you input")
    quit()
else:
    print("there is no vowel in the string you input")
        
