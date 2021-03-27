selling_price=int(input("enter the sp"))
cost_price=int(input("enter the cp"))
if selling_price>cost_price:
    amt=selling_price-cost_price
    print("profit",amt)
elif cost_price>selling_price:
    amt=cost_price-selling_price
    print("loss",amt)
else:
    print("invalid sp and cp")
