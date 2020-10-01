a=int(input('Введите год :  '))

if a%4==0 and a%100==0 and a%400==0:
    print('Год Високосный')
elif a%4==0 and a%100==0:
    print('Год  Не Високосный')
elif a%4==0:
    print('Год Високосный')
else:
    print('Год  Не Високосный')
        


