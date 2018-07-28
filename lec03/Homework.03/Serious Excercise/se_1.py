shop=["T-shirt","Skirt"]
while True:
    print("Our items: ")
    for i,j in enumerate(shop):
        print("{}. {}".format(i+1,j))
    lam=input("Welcome to our shop, what do you want? (C,R,U,D) ")
    if lam == "C":
        shop.append(input("Enter new item: "))
    elif lam == "R":
        print()
    elif lam=="U":
        shop[int(input("Update position? "))-1]=input("New item? ")
    elif lam=="D":
        shop.pop(int(input("Delete position? "))-1)
    else:
        break
    