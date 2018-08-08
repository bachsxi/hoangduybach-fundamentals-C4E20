so=int(input("Enter a number: "))
n=1
loop=True
while loop:
    if so**2 >10**n:
        loop=False
    else:
        n+=1
    for i in range(1,(so+1)):
        for j in range(i,(so+1)*i,i):
            if j <10:
                print(j,end="  ")
            elif j>=10:
                print(j,end=" ")
        print()   
    loop=False