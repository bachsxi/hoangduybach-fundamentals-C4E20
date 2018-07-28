for i in range(1,10):
    for j in range(i,10*i,i):
        if j <10:
            print(j,end="  ")
        elif j>=10:
            print(j,end=" ")
    print()   
    