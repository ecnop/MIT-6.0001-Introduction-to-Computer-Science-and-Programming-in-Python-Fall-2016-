n = int(input("Enter an integer: "))
root = 1
pwr = 1
ans = 0
while root < n:
    while pwr < 6 and root**pwr <= n:
        if root**pwr == n:
            print ("Root =",root,"Power =",pwr)
            break
        pwr = pwr + 1
    if root**pwr == n:
        break
    root = root + 1
    pwr = 1
if root**pwr != n:
    print("No two pairs of numbers exist such that...")
elif root == n:
    print ("Root =",root,"Power =",pwr)
    