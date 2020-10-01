a=int(input('Введите перввый член прогрессии: '))
b=int(input('Введите знаменатель: '))
c=int(input('Введите длину прогресси: '))
x=0
print(a,end=' ')
c=c-1
while x<c:
    x+=1
    a=a*b
    print(a,end=' ')