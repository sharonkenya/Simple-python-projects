num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2 and num1 > num3:
    print("First number is the greatest")
if num2 > num1 and num2 > num3:
    print("Second number is the greatest")
if num3 > num1 and num3 > num2:
    print("Third number is the greatest")
