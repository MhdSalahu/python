class stdone:
    def name(std):
        sdname=input("Enter your name : ")
        print("Your name is "+sdname)
    def mark(std):
        sub=[]
        for i in range(0,5):
            mark=int(input("\nEnter the mark : "))
            sub.append(mark)
        print(sub)
        total=sum(sub)
        print("Total mark = ",total)
        perc=float((total/500)*100)
        print(perc," %")

class stdtwo:
    def name(std):
        sdname=input("Enter your name : ")
        print("Your name is "+sdname)
    def mark(std):
        sub=[]
        for i in range(0,5):
            mark=int(input("\nEnter the marks : "))
            sub.append(mark)
        print(sub)
        total=sum(sub)
        print("Total mark = ",total)
        perc=float((total/500)*100)
        print(perc,"  %")

def func(obj):
    obj.name()
    obj.mark()

ob1 =stdone()
ob2=stdtwo()
func(ob1)
func(ob2)