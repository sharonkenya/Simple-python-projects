#create a Python Program to check if a given year is a leap year
#The year is divisible by 4 but not divisible by 100
#except_if its also divisible by 400
year=int(input("Enter the year: "))
if year%4==0 and (year%100!=0 or year%400==0):
    print("This is a leap year")
else:
    print("This is not a leap year")
