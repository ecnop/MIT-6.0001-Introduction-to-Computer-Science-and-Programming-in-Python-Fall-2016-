

def isIn (str1,str2):
    return str1 in str2 or str2 in str1
    

x = input("Enter a string: ")
y = input("Enter a string: ")

print(isIn(x,y))