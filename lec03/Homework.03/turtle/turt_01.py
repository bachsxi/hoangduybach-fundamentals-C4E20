from turtle import *
mau = ['red', 'blue', 'brown', 'yellow', 'grey']
n=1
for j in range(len(mau)):
    color(mau[j])
    for i in range (n+2):
        forward(100)
        left(180-180*n/(n+2))
    n+=1
mainloop()

