m=[202,1,203,10,203,201,432,2,4302,4032,0,340,62,60,-2]
n=len(m)
o=m[0]
s=m[0]
for x in range(1,n):
    if m[x]>o:
        o=m[x] 
for y in range(1,n):
    if m[y]<s:
        s=m[y]
    
print("the hieghst in the array is",o,"and the lowest is",s)
