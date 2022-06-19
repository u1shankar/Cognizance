import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering' ,'chennai' , 'campus'])
k,f="",""
for i in ser: 
    k=i
    f=k[0]
    k=f.upper()+k[1:]
    print(k,end=" ")    