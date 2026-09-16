
marks =int(input("Enter your marks:"))

if (marks>=90 and marks<=100):
    print("GRADE: A")
elif (marks<90 and marks>=80):
    print("GRADE: B")

elif (marks<80 and marks>=70):
    print("Grade: c")

elif (marks<70 and marks>=60):
    print("Grade: D")

else:
    print("FAIL")