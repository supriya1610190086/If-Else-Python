num=int(input("enter the number"))
if num%5==0:
    print("divisible by 5")
if num%15==0:
    print("divisible by 15")
if num%5==0 and num%15==0:
    print("divisible by both 5 and 15")
else:
    print("Invalid number")