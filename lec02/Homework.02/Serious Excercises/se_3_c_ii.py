so=int(input("Enter a number: "))
for i in range(1,(so+1)):
    for j in range(i,(so+1)*i,i):
        # loop = True
        # while True:
            # n=1
            # if so**2 > 10*n:
            #     n+=1
            # else:
            #     loop= False
        if j <10:
            print(j,end="  ")
        elif j>=10:
            print(j,end=" ")
    print()   
