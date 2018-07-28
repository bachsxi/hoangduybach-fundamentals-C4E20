flock=[234,2342,1,12,312,23,63]
print("Hello my name is Bachs and these are mine ships size: ")
print(*flock,sep=", ")
n=int(input("Enter the month you want to sell the flock: "))
for j in range(n+1):
    if j!=0:
        print("MONTH",j,":")
        print("One month has passed, now here is my flock: ")
        for i in range (len(flock)):
            flock[i]+=50    
        print(*flock,sep=", ")
    flock.sort()
    print("Now my biggest ship has size",flock[-1],"let's shear it")
    print("After shearing here is my flock: ")
    flock[-1]=5
    print(*flock,sep=", ")
total=0
for i in range(len(flock)):
    total= total + int(flock[i])
print("The total size of my flock is:",total)
print("I would get",total,"*2 =",total*2,"$")
