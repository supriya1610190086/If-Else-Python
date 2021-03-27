Girls=int(input("enter the girls"))
if Girls==12:
    print("room is occupied")
elif Girls<12:
    print(12-Girls,"Bad are left")
else:
    print(Girls-12,"These many girls shift them in other room")