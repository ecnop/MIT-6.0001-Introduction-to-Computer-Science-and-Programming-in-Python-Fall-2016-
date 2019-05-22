print("Please enter 10 integers")

x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
x6 = int(input())
x7 = int(input())
x8 = int(input())
x9 = int(input())
x10 = int(input())

array=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]

i = 0
ans = 0

while (i < 10):
    if array[i] % 2 == 1:
        if array[i] == x1:
            ans = x1
        else:
            if array[i] > ans:
                ans = array[i]
    i = i + 1

if ans != 0:    
    print("The largest odd number is",ans)
else:
    print("There were no odd numbers in the set")