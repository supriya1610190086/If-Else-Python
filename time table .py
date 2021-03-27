time=float(input("enter the time"))
if time>6  and time<7:
    print("morning exercise")
elif time>=7 and time<=8.30:
    print("break time")
elif time>=8.30 and time<9.30:
    print("english activity")
elif time>=9.30 and time<1:
    print("coding time")
elif time>1 and time<2.30:
    print("lunch break")
elif time>=2.30 and time<4:
    print("culture activity")
elif time>=4 and time<4.30:
    print("break time")
elif time>=4.30 and time<9:
    print("coding time")
else:
    print("invalid time")