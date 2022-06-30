import string
f=open("onelinefile.txt","r")
s=str(f.read())
fi=len(s)
temp=""
c=0
for i in range(fi):
    if s[i].isalpha()==True:
        temp+=s[i]
        #print(temp)
        if i+1<fi:
            if s[i+1].isalpha()!=True:
                if c!=3:
                    temp+=","
                c+=1
    elif s[i].isdigit()==True:
        temp+=s[i]
        if s[i+1]==".":
            temp+="."
        elif s[i+1].isdigit()!=True and s[i+1]!=".":
            if c!=3:
                temp+=","
            c+=1
    if c%4==0:
        temp+="\n"
        c=0
f.close()
f2=open("Filename2.csv","w")
f2.writelines(temp)
f2.close()
print("The lines written in the file are\n"+temp)

    
