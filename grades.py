marks=int(input("Enter Student's marks: "))
if marks>80 and marks<=100:
    print("You scored an A")
elif marks>60 and marks<=80:
    print("You scored a B")
elif marks > 40 and marks <= 60:
    print("You scored a C")
elif marks > 30 and marks <=40:
    print("You scored a D")
elif marks>0 and marks<=30:
    print("You failed!!")
else:
    print("WRONG INPUT")


