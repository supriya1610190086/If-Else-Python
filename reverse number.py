num = int(input("enter the number"))
reverse=int(str(num)[::-1])
if num!=0:
    reverse=reverse*1
    print(reverse)
else:
    print("given input is a not a number")