def my_function(x, y):

    if x > y:
        smaller = y
    else:
        smaller = a
    for i in range(1, smaller + 1):
        if ((a % i == 0) and (b % i == 0)):
            hcf = i

    return hcf


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The H.C.F. of", num1, "and", num2, "is", my_function(num1, num2))