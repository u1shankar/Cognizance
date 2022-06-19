import numpy as np
a=int(input("First number: "))
b=int(input("Last number: "))
l=[]
for i in range(a,b+1):
    l.append(i)
vec1=np.array(l)
k=[]
j=0
for i in range(0,5*len(l)+1):
    if (i%6==0 and j<len(l)):
        k.append(vec1[j])
        j+=1
        if j==len(l):
            break
    else:
        k.append(0)
vec=np.array(k)
print("The Final Vector:")
print(vec)

