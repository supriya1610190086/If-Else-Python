num=int(input("enter the number"))
a=num%10
b=(num//10)%10
c=(num//10)//10
d=a+b+c
if num%d==0:
    print(num,"It is harshad number")
else:
    print(num,"It is not harshad number")