a=int(input('Введите коэффициент a: '))
b=int(input('Введите коэффициент b: '))
c=int(input('Введите коэффициент c: '))
x=int()
ur=a*x**2+b*x+c
D=b**2-4*a*c

if D>0:
    D=D**0.5
    print('Два корня',end=' ')
    up=-b+D
    down=-b-D
    a=2*a
    x=up/a
    print('Первый корень= ',x)
    x=down/a
    print('Второй корень= ',x)
elif D==0:
    a=2*a
    x=-b/a
    print('Один корень')
    print('Корень равен=', x)
else:
    print('Нет корней')
    
