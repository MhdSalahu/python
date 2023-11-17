num= int(input("Enter the number : "))

def fact(num):
    if(num<0):
        return 0
    elif num==0 or num==1 :
        return 1
    else:
        f=1
        while(num>0):
            f=f*num
            num=num-1
        return f
f=fact(num)
print("factorial = ",f)

