from random import choice
words=["champion","hello","fundamental","sixautrai"]
word= choice(words)
chars=list(word)
updated_chars=[]
loop= True
while loop:
    rand_char = choice(chars)
    updated_chars.append(rand_char)
    chars.remove(rand_char)
    if len(chars)==0:
        loop= False
print(*updated_chars)
ans= input("your guess: ")
if ans==word:
    print("Huraaa")
else:
    print(":<")