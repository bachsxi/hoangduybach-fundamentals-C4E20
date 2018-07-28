from turtle import *
mau= ['red', 'blue', 'brown', 'yellow', 'grey']
for i in range(len(mau)):
    color(mau[i])
    begin_fill()
    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()
mainloop()    