flock=[234,2342,1,12,312,23,63]
print("Hello my name is Bachs and these are mine ships size: ")
print(*flock,sep=", ")
flock.sort()
print("Now my biggest ship has size",flock[-1],"let's shear it")