f=open("about.txt","r")
fi=f.read()
l=list(fi.split(" "))
temp=[]
for i in l:
   if len(i)>=6:
    temp.append(i)
c=0
count=[]
for i in temp:
    c=temp.count(i)
    count.append(c)
i=count.index(max(count))
print("The most frequently occured element is: ",temp[i])
print("It has occured",count[i],"times")