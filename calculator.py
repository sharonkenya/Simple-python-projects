num1=int(input("Enter the first number: "))
operator=(input( "Operator: "))
num2=int(input("Enter the second number: "))
if operator=="+":
    print(num1, "+", num2, "=", num1+num2)
elif operator=="-" :
    print(num1, "-", num2, "=", num1-num2)
elif operator=="*":
    print(num1, "*", num2, "=", num1 * num2)
elif operator=="/":
    print(num1, "/", num2, "=", num1/num2)
elif operator == "%":
    print(num1, "%", num2, "=", num1 % num2)
else:
    print("SYNTAX ERROR")

