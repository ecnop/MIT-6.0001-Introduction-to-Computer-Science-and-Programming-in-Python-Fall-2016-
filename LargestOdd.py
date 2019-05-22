print("Enter three numbers:")
x = int(input())
y = int(input())
z = int(input())
if x%2 == 1 and y%2 == 1 and z%2 == 1:
    if x > y and x > z:
        print(x)
    elif y > z:
        print(y)
    else:
        print(z)
elif x%2 == 1 and y%2 == 1 and z%2 == 0:
    if x > y:
        print(x)
    else:
        print(y)
elif x%2 == 0 and y%2 == 1 and z%2 == 1:
    if y > z:
        print(y)
    else:
        print(z)
elif x%2 == 1 and y%2 == 0 and z%2 == 1:
    if x > z:
        print(x)
    else:
        print(z)
elif x%2 == 1:
    print(x)
elif y%2 == 1:
    print(y)
elif z%2 == 1:
    print(z)
else:
    print("None of the numbers are odd")
    
        
        