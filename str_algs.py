def chng(l):
    str1=''
    for i in range(len(l)):
        str1 += l[-i-1]
    return str1


l='Hello, world!'
str2=chng(l)
print(str2)
