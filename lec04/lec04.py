num=int(input("Nhập số của bạn đê: "))
low=0
high=100
loop=True
while loop:
    mid=(low+high)//2
    print("Số của m có phải",mid,"không?")
    answ=input()
    if mid!=num:
        if answ=="s":
            high=mid
        elif answ=="h":
            low=mid
        else:
            print("Điêu vãiii")
    elif mid==num:
        if answ=="c":
            print("tui biết mà")
        else:
            print("đừng điêu chính là số",num)
        loop=False
    

    
