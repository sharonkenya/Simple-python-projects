# Write a python program to calculate te ticket price for a movie theatre based on the age of the customer
# 0-5 free
# 6-12 500
# 13-17 1000
# 18+ 1500
age=int(input("Enter customer's age: "))
if age>=18:
    print("Ticket price=1500")
elif age >=13 and age<18:
    print("Ticket price=1000")
elif age>=6 and age<13:
    print("Ticket price=500")
elif age>=0 and age<6:
    print("Ticket is FREE")
else:
    print("Invalid age")