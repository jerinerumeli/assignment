from sys import argv


print ('Number of inputs:', len(argv)-1)
# print ('Argument List:', str(sys.argv))
list1=argv[1:]

big=0
fl=1
for x in list1:
    if(x.isdigit()):
            if(big<int(x)):
                big=int(x)
    else:
        print(x,"is not a number")
        fl=0
        break
if(fl!=0):
    print("biggest of",len(argv)-1," :",str(big))

    