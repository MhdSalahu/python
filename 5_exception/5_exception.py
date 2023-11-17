a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("\n\t1.Add\n\t2.Sub\n\t3.Product\n\t4.division\nEnter your choice(1-4): "))

if c==1:
    print("sum = ",a+b)
elif c==2:
    print("Sub = ",a-b)
elif c==3:
    print("Product = ",a*b)
elif c==4:
    try:
        div=a/b
        print(" Division = ",div)
    except:
        print("Not defined ")
else:
    print("Wrong input")
    
