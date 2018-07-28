total=1
loop=True
while (loop==True):
    num=int(input("Enter a number: "))
    if num>0:
        print(num,"!=",end="")
        for i in range (1,num):
            total=total*i
            print(i,"x",end=" ")
        total=total*num
        print(num,"=",total)
        print("The fractional of",num,"is",total)
        loop= False
    elif num ==0:
        total=1
        print(num,"!=",total)
        print("The fractional of",num,"is",total)
        loop=False
    else:
        print("Invalid number try again")