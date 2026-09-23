# greatest of three numBER

A = int(input("Enter number A:"))
B = int(input("Enter number B:"))
C = int(input("Enter number C:"))

if (A>=B and A>=C):
    print("A is the greatest number")

elif (B>=A and B>=C):
    print("B is the greatest number")

else:
    print("C is the greatest number")