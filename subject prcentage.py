Physics=int(input("enter the mark is physics"))
Chemistry=int(input("enter the mark is chemistry"))
Biology=int(input("enter the mark is biology"))
Mathmatics=int(input("enter the mark is mathmtics"))
Computer=int(input("enter the mark is computer"))
per=(Physics+Chemistry+Biology+Mathmatics+Computer)/5.0
print(per)
if per>=90 and per<=100:
    print("Grade A")
elif per>=80 and per<90:
    print("Grade B")
elif per>=70 and per<=80:
    print("Grade C")
elif per>=60 and per<=70:
    print("Grade D")
elif per>=40 and per<=60:
    print("Grade E")
elif per<40 and per>=1:
    print("Grade F")
else:
    print("Invalid percentage")