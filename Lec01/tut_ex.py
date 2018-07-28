n=int(input("so canh "))
from turtle import *
speed(-1)
shape("turtle")

color("violet")
for i in range(1000):
    for i in range(n):
        forward(100)
        left(360/n)
    pu()
    left(60)
    forward(20)
    pd()
    right(60)

    


mainloop()