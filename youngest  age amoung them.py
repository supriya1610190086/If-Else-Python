age1=int(input("enter the first age"))
age2=int(input("enter the second age"))
age3=int(input("enter the third age"))
if age1>=age2 and age1>=age3:
    print("youngest is first age",age1)
elif age2>=age1 and age2>=age3:
    print("youngest is second age",age2)
elif age3>=age1 and age3>=age2:
    print("youngest is third age",age3)
else:
    print("all are equal")

