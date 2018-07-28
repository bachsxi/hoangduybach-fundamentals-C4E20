print("Welcome to the Body evaluation session! ")
cao=int(input("Your height in cm: "))
nang=int(input("Your weight in kg: "))
cao= cao/100
BMI= nang/(cao*cao)
if BMI < 16:
    print(BMI,"< 16 = You're severely UNDERWEIGHT!")
elif BMI <=18:
    print("Your BMI is ",BMI," is between 16 and 18.5 = You're UNDERWEIGHT!")
elif BMI <=25:
    print("Your BMI is ",BMI," is between 18.5 and 25 = You're NORMAL!")
elif BMI <=30:
    print("Your BMI is ",BMI," is between 25 and 30 = You're OVERWEIGHT!")
else:
    print("You're just FAT!")

