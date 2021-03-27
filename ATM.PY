BALANCE="20000"
print(BALANCE)
print("******************WELCOME*********************")
print("******************TO ATM**********************")
ATM_CARD = input ("enter the atm card")
if ATM_CARD == "insert the atm card":
    print("correct")
    language =  input("enter the language")
    if language =="hindi" or "english" or "marathi":
        print("your choose launguage is correct")
        account = input("enter the account type")
        if account == "saving" or account == "current":
            print("ok")
            pin_code = int(input("enter the pin code"))
            if pin_code==1234:
                print("correct")
                amount_cash = int(input("enter the amount cash"))
                if amount_cash>0 and amount_cash<20000:
                    print(amount_cash,"withdraw money")
                    print(20000-amount_cash,"remaining money in ATM")
                else:
                    print(amount_cash,"This amount is not your account")
            else:
                print("This is not your pin code")  
        else:
            print("This is not account")
    else:
        print("incorrect launguage")
else:
    print("this is not atm card")
                    
