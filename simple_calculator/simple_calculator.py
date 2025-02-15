print("This is simple calculator")

num1=int(input("Enter first number:\n"))

opt=input("Opration\n")

num2=int(input("Enter second number:\n"))

if (opt=="+"):
    print(num1,"+",num2,"=",num1+num2)
elif (opt=="-"):
    print(num1,"-",num2,"=",num1-num2)
elif(opt=="*"):
    print(num1,"X",num2,"=",num1*num2)
elif(opt=="/"):
    print(num1,"/",num2,"=",num1/num2)
else:
    print("somethong went wrong")
