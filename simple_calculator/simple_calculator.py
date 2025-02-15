print("This is simple calculator")

num1=int(input("Enter first number:"))

#print("Enter \n 1:addition \n 2:subtraction \n 3:multiplication \n 4:division")
opt=input("Opration")

num2=int(input("Enter second number:"))

if (opt=="+"):
    print(num1+num2)
elif (opt=="-"):
    print(num1-num2)
elif(opt=="*"):
    print(num1*num2)
elif(opt=="/"):
    print(num1/num2)
else:
    print("somethong went wrong")





""""tup=[1,4,9,16,25,36,49,64,81,100]

x=int(input("Enter number to search:"))

idx=0

while idx < len(tup):
    if(tup[idx]==x):
        print("FOUND at inx",idx)
        break
    idx+=1
if(idx==len(tup)):
    print("NOT FOUND")"""

