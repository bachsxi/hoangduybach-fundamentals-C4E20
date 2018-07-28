so=int(input("Enter a number: "))
so2=so//2
if so%2 !=0:
    for i in range(so2):
        print(" 1 0"*so2,"1")
        print(" 0 1"*so2,"0")
    print(" 1 0"*so2,"1")
else:
    for i in range(so2):
        print("1 0 "*so2)
        print("0 1 "*so2)
