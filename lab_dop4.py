a=int(input())
b=2

if a>0:
    while a/b!=1:
        if a%b==0:
            a/=b
            print(b)
        else:
            b+=1
    print(b)
else:
    print('число не натуральное')


