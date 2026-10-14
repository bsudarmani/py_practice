import math
while True:
    print("=========MENU===========")
    ch=int(input("\n1.square root \n2.fact \n3.power \n4.abs \n5.floor \n6.ceil \n7.sin \n8.cos \n9.log10 \n10.gcd \n11.exit"))
    if ch==1:
        val=float(input("Enter the number"))
        if val>0:
            print(math.sqrt(val))
        else:
            print("invalid choice")
    elif ch==2:
        val=int(input("Enter the value"))
        if val>0:
            print(math.factorial(val))
        else:
            print("invalid choice")
    elif ch==3:
        base=float(input("Enter the base value"))
        expo=float(input("Enter the expo value"))
        print(math.pow(base,expo))
    elif ch==4:
        val=float(input("Enter the abs value"))
        print(math.fabs(val))
    elif ch==5:
        val=float(input("Enter the floor value"))
        print(math.floor(val))
    elif ch==6:
        val=float(input("Enter the ceil value"))
        print(math.ceil(val))
    elif ch==7:
        sin=float(input("Enter the sin value"))
        radian=math.radians(sin)
        print(math.sin(radian))
    elif ch==11:
        break
