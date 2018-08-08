menu=["mathematics","physics","literatures","geography"]
menu2=[]
import random
tu=random.choice(menu)
tu_list = list(tu)
loop= True
while len(tu_list) != 0:
    chu=random.choice(tu_list)
    menu2.append(chu)
    tu_list.remove(chu)
    # print(chu)
    # print(menu2)
#     (list(tu)).remove(chu)
#     if len(list(tu))==0:
#         loop= False
print(*menu2)