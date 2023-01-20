
from sys import argv

def count_words(x,di,len):
    
    cnt=0
    j=0
    while(len!=0):
        if(x==di[j]):
            cnt=cnt+1
            j=j+1
            len=len-1
            
        else:
            j=j+1
            len=len-1
    return(cnt)


sentance=argv[1:]
sp_words=sentance

length=len(sp_words)
j=length
list=['']
dict={}
fl=0
i=1

for x in sp_words:
    
    
       dict[i]=x
       i=i+1
print(dict)       


value=0
for x in sp_words:
    cnt=count_words(x,sp_words,length)
    if(cnt>value):
        value=cnt
        rword=x
print("most repeated word is : ",rword)
    
    
