a=int(input('Введите первую сторону: '))
b=int(input('Введите вторую сторону: '))
c=int(input('Введите третью сторону: '))


if a+b>c and a+c>b and b+c>a:
    print('Треугольник существует: ',end='')
    
    
    if a!=b and a!=c and b!=c:
        print('разносторонний')
    
    
    
    elif a==b!=c or a==c!=b or b==c!=a:
        print(' равнобедренный')
    
    
    
    elif a==b==c:
        print('равносторонний')


else:
    print('Треугольника не существует!')