#ceaser cipher
str="india"
index=0
while index<len(str):
    letter=str[index]
    print(chr(ord(letter)+2),end=" ")
    index+=1