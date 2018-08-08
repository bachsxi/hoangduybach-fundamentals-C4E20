teen_code= {
    "hc":"hông có",
    "cc":"cục cưng",
    "lm":"làm",
    "any":"anh người yêu",
    "eny":"em người yêu",
    "ns":"nói",
    "r":"rồi",
}
loop= True
while loop:
    for key in teen_code.keys():
        print(key,end="\t")
    print()
    print("_" * 30)
    trans= input("Từ muốn dịch: ")
    if trans in teen_code:
        print("Dịch nghĩa:", teen_code[trans])
        
    else:
        add=input("Từ chưa có trong từ điển có muốn thêm vào không? Y/N: ").upper()
        if add== "Y":
            teen_code[trans]=input("Nhập nghĩa của cụm từ: ")
            print("Đã thêm vào!")
        else:
            break
    print("_" * 30)
