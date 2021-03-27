Class_held=int(input("enter the class held"))
Class_Attendence=int(input("enter the class attendence"))
Attendence=(Class_Attendence/(Class_held))*100
print("Attendence is",Attendence)
if Attendence>=75:
    print("you are allowed sit in exam",)
else:
    print("sorry,you are not allowed exam,attend more classes from next time")
