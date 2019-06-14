p = float(input('Тиск у паскалях: '))
v = float(input('обєм'))
r = 8.314
f = input('цельсіях чи кельвін ')
t = float(input('Температура'))

if f == 'цельсіях':
    a = t+273.15
    n = (p*v)/(r*a)
    print(n)
elif f == 'кельвін':
    n = (p*v)/(r*t)
    print(n)

import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny Yaroslav')    
          
