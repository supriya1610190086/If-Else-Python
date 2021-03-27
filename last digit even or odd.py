num=int(input("enter the number"))
last_digit=num%10
if last_digit%2==0:
    print("even number",last_digit)
else:
    print("odd number",last_digit)