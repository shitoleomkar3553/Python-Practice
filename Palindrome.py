list = ["r", "a", "c", "e", "c", "a", "r" ]

copy_list = list.copy()
copy_list.reverse()

if(copy_list == list):
    print("palindrome")

else:
    print("Not palindrome")