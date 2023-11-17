def multiplication(n):
    if(n==0):
        return 0
    else:
        for i in range(1,11):
            a=int(i*n)
            print(i," X ",n," = ",a)

