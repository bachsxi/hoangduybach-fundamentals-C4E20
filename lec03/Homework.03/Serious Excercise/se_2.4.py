flock=[234,2342,1,12,312,23,63]
print("Hello my name is Bachs and these are mine ships size: ")
print(*flock,sep=", ")
flock.sort()
print("Now my biggest ship has size",flock[-1],"let's shear it")
print("After shearing here is my flock: ")
flock[-1]=5
print(*flock,sep=", ")
print("One month has passed, now here is my flock: ")
for i in range (len(flock)):
    flock[i]+=50
print(*flock,sep=", ")