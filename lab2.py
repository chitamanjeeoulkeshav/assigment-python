a = int(input("Enter four number in the first list"))
al = a.split()
b = int(input("Enter four number in the second list"))
bl = a.split()
c = int(input("Enter four number in the third list"))
cl = a.split()
d = int(input("Enter four number in the forth list"))
dl = a.split()

def sum1(a1):
    for num1 in al:
        global s1
        s1 = int(s1) + int(num1)
    return s1

def sum2(bl):
    for num2 in bl:
        global s2
        s2 = int(s2) + int(num2)
    return s2

def sum3(cl):
    for num3 in cl:
        global s3
        s3 = int(s3) + int(num3)
    return s3

def sum4(d1):
    for num4 in dl:
        global s4
        s4 = int(s4) + int(num4)
    return s4


x = sum1(al)
y = sum2(bl)
z = sum3(cl)
h = sum4(dl)
li = (x, y, z, h)

max1 = -9999
for num in li:
    if num > max1:
        max1 = num

if max1 == s1:
    print(al)
elif max1 == s2:
    print(bl)
elif max1 == s3:
    print(cl)
elif max1 == s4:
    print(dl)