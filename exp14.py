feet=int(input("Enter length in feet:"))
while True:
    print('\n1.Inches')
    print('2.Yards')
    print('3.Miles')
    print('4.Millimeters')
    print('5.Centimeters')
    print('6.Meters')
    print('7.Kilometers')
    print('8.exit')
    ch=int(input("Enter your choice:"))
    if ch==1:
        res=feet*12
    elif ch==2:
        res=feet/3.0
    elif ch==3:
        res=feet/5280.0
    elif ch==4:
        res=feet*304.8
    elif ch==5:
        res=feet*30.48
    elif ch==6:
        res=feet*0.3048
    elif ch==7:
        res=feet*0.0003048
    elif ch==8:
       print("Existing program.....")
       break
    else:
       print("Invalid choice!Try again.")
       continue
    print("The required result=",res)

    

 


