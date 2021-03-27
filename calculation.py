num_1=int(input("enter the first number"))
num_2=int(input("enter the second number"))
symbol=input("operator")
if symbol=="+":
    print(num_1+num_2,"add")
elif symbol=="-":
    print(num_1-num_2,"sub")
elif symbol=="*":
    print(num_1*num_2,"mul")
elif symbol=="/":
    print(num_1/num_2,"div")
elif symbol=="//":
    print(num_1//num_2,"floor div")
elif symbol=="**":
    print(num_1**num_2,"exponent")
else:
    print("invalid operator")