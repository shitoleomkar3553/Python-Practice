# CGPA calculator

marks =int(input("Enter your marks:"))

if (marks>=90 and marks<=100):
    print("CGPA is 9.00")

elif (marks>=80 and marks<90):
    print("CGPA is 8.00")

elif (marks>=70 and marks<80):
    print("CGPA is 7.00")

elif (marks>=60 and marks<70):
    print("CGPA is 6.00")

else:
    print("You are fail")