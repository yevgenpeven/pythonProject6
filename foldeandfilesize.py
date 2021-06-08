import os
from glob import glob

#path, size = input('Дай линку и формат вывода через пробел ').split()

path = input('Введите адрес: ')
size = input('Вывод результата в b, kb, mb:')


if size == 'b':
    if os.path.isfile(path):
     print('ФАЙЛ')
     print('Размер:', os.path.getsize(path) ,'b')
    elif os.path.isdir(path):
        print('Список объектов в нем: ')
        for file in glob(f'{path}\*'):
         print(os.path.basename(file), os.path.getsize(file),'b')
    else:
        print("Не верно указано адресc")

elif size =='kb':
    if os.path.isfile(path):
        print('ФАЙЛ')
        print('Размер:', round((os.path.getsize(path) / 1024), 2), 'kb')
    elif os.path.isdir(path):
        print('Список объектов в нем: ')
        for file in glob(f'{path}\*'):
         print(os.path.basename(file), round((os.path.getsize(file) / 1024), 2), 'kb')
    else:
        print("Не верно указано адрес")
elif size == 'mb':
    if os.path.isfile(path):
         print('ФАЙЛ')
         print('Размер:', round((os.path.getsize(path) / 1048576), 2), 'mb')
    elif os.path.isdir(path):
         print('Список объектов в нем: ')
         for file in glob(f'{path}\*'):
          print(os.path.basename(file), round((os.path.getsize(file) / 1048576), 2), 'mb')
    else:
        ("Не верно указано адрес")
else:
 print('Спробуй ще')