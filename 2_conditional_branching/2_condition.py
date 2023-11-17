age=int(input("Enter your age : "))
if age<18:
    print("You'r minor...You're not eligible for work")
else:
    if age>=18 and age<=60 :
        print("You are eligible for work")
    else:
        print("You are too old to work as per Government rule")
        print("Please collect your pension")