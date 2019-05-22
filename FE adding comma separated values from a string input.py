x = input("Enter a string for the exercise: ")
n = ""
ans = 0
counter = 1
for i in x:
    print(i, ans)
    if i == ",":
        ans = ans + float(n)
        n = ""
#    elif i != "," and i != x[-1]:
#        n = n + i
#    else:
    elif counter == (len(x)):
        n = n + i
        ans = ans + float(n)
    else:
        n = n + i
    counter = counter + 1
print("The sum of the numbers is",ans)