Question=input("enter the Question")
Answer=input("enter the Answer")
if Question=="what time is the meeting tomorrow:" and Answer=="10 am tomorrow":
    print(Question+Answer)
elif Question=="who will attend:" and Answer=="the general director or managers":
    print(Question+Answer)
elif Question=="what will the meeting be about:" and Answer=="regarding the issue of employee salaries":
    print(Question+Answer)
else:
    print("invalid question answer")