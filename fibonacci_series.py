from sys import argv

check_num=int(argv[1])
num1=0
num2=1
pos=0
fl=0
if(check_num==num1):
    pos=1
if(check_num==num2):
    pos=2
if(pos==0):
    
    while(check_num>=num2):
        if(check_num==num2):
            pos=pos+1
            fl=1
            break
        else:
            temp=num2
            num2=num1+num2
            num1=temp
            pos=pos+1
            
if(fl!=0 and pos!=0):
    
        print(check_num," in the ",pos+1," position")
elif(pos!=0 and fl!=0):
    print(check_num," in the ",pos," position")
else:
    print(-1)

