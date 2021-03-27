water=int(input("enter the water"))
if water<=1:
    print("water fill")
elif water>1 and water<10:
    print("water not fill")
elif water>10:
    print("overflow")