from turtle import *
speed(-1)
n=1
for j in range(4):
    if n%2==1:
        color("blue")
    elif n%2==0:
        color("red")
    for i in range (n+2):
        forward(100)
        left(180-180*n/(n+2))
    n+=1
mainloop()