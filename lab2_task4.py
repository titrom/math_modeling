x=0
a=0
b=1
c=float(input('Введите количество чисел в порядке: '))

print(b,end=' ')
if c>0:
    while x<c//2:
        x+=1
        a=a+b
        b=b+a
        print(a,b,end=' ')
else:
    print('Введино неправильное число')

