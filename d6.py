print("\n\n")
print("1.creation of tupple")
print("2.concatination")
print("3.repeatation")
print("4.range slicing")
print("5.slicing")
print("6.string membership")
print("7.length of tupple")
print("8.maximum value of tupple")
print("9.delete a tupple")
print("\n\n")
while True:
    choice=int(input('enter your choice'))
    if choice==1:
        t1=()
        print(t1)
    if choice==2:
        t1=tuple(input("enter tupple 1"))
        t2=tuple(input("enter tupple 2"))
        print(t1+t2)
    if choice==3:
        a=tuple(input('ënter the tupple'))
        n=int(input("how many times to repeat"))
        print("the entire",a,"is repeated",n,"times","\n the value is",a*n)
    if choice==4:
        t1=tuple(input("enter tupple 1"))
        c=int(input('from where'))
        d=int(input('to where'))
        print(t1[c:d])
    if choice==5:
        t1=tuple(input("enter tupple 1"))
        g=int(input('from where'))
        print(a[i])
    if choice==6:
        t1=tuple(input("enter tupple 1"))
        f=input("enter string to check")
        print(f in t1)
    if choice==7:
        t1=tuple(input("enter tupple 1"))
        print(len(t1))
    if choice==8:
        t1=tuple(input("enter tupple 1"))
        z=max(t1)
        print(z)
    if choice==9:
        t1=tuple(input("enter tupple 1"))
        del t1s
        
        
        
        
        
        
        
    
    
        
