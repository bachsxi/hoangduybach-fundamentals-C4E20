print("Hello please login to continue: ")
n=0
loop=True
while True:
    usnm=input("Enter your username: ")
    if usnm=="c4eBach": 
        passwd=input("Enter your password: ")
        if passwd=="1234321":5
            print("Successfully login, Hello",usnm)
            break
        else:
            print("Incorrect Password try again! ")
    else:
        print("Incorrect Username try again!")
    print("You have",2-n,"attemps left")
    n+=1
    if n==3:
        print("Banned")
        break
    