list = []

val_1 = input("Enter your value:")
val_2 = input("Enter your value:")
val_3 = input("Enter your value:")
val_4 = input("Enter your value:")
val_5 = input("Enter your value:")

list.append(val_1)
list.append(val_2)
list.append(val_3)
list.append(val_4)
list.append(val_5)

copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("Palindrome")

else:
    print("Not palindrome")