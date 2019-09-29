num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
numbers_min = min(num1, num2)
while(1):
    if(numbers_min % num1 == 0 and numbers_min % num2 == 0):
        print("LCM of two number is: ", numbers_min)
        break
    numbers_min += 1