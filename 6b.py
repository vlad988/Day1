a = input('Де проживаєте?: будинок, гуртожиток, квартира ')
b = float(input('Час який ви вдома '))
if a == 'будинок' and b >= 18:
    print('В’єтнамське порося')
elif a == 'будинок' and 10 >= b >= 17:
    print('Собака')
elif a == 'будинок' and b < 10:
    print('Змія')
elif a == 'квартира' and b > 10:
    print('Кішка')
elif a == 'квартира' and b < 10:
    print('Хом’як')
elif a == 'гуртожиток' and b > 6:
    print('Рибки')
elif a == 'гуртожиток' and b < 6:
    print('Мурашник')

import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny Yaroslav')    
          

