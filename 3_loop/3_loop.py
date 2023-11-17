lower = int(input("Enter lower range : "))
upper = int(input("Enter upper range : "))
even=[]
odd=[]

for i in range(lower,upper+1):
    if(i%2==0):
      even.append(i)
    else:
      odd.append(i)
print("Odd numers are : ")
print(odd)
print("Even numers are : ")
print(even)


    