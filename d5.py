while True:
    print("1.repeatation")
    print("2.reversing")
    print("3.concatinating")
    print("4.member of string")
    print("5.slicing")
    print("6.range slicing")
    print("7.splitting")
    print("8.counting occurance")
    print("9.capitalize")
    choice=int(input('enter your choice from (1-9'))
    a=input("sentence")
    if choice==1:
        n=int(input("how many times to repeat"))
        print("the entire",a,"is repeated",n,"times","\n the value is",a*n)
    elif choice==2:
        print(a[1],"\n")
    elif choice==3:
        e=input("sentence second")
        print(a+e)
    elif choice==4:
        f=input("enter string to check")
    elif choice==5:
        g=int(input('from where'))
        print(a[i])
    elif choice==6:
        h=int(input('from where'))
        i=int(input('to where'))
        print(a[h:i])
    elif choice==7:
        b=a.split(',')
        print (b)
    elif choice==8:
        u=input('alphabet to count')
        x=a.count(u)
        print()
    elif choice==9:
        z=a.upper()
        print(z)
        
        
        
     
