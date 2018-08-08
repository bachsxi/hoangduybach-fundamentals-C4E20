num=int(input("Enter a number: "))
is_prime=True
loop= True
i=2
while loop:
    if num%i==0:
        is_prime= False
    i+=1
    if i == num:
        loop= False
if is_prime:
    print("{} is a prime number".format(num))
else:
    print("{} is not a prime number".format(num))
