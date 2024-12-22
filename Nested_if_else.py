#WAP For Find Greatest Of Three No.(Nested If Else)
a = int(input("enter Your Value A"))
b = int(input("enter Your Value B"))
c = int(input("enter Your Value C"))

if  a>b:
    print(f"a is Greater")
elif  a>c:
    print(f"b is Greater")       
else:
    if b>c:
        print(f"b is Greater")
    else:
        print(f"c is greater")