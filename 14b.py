import math
t = float(input('температура повітря '))
v = float(input('швидкість вітру '))
if t <= 10 and v >= 4.8:
    wci = 13.12 + 0.6215 * t - 11.37 * v**0.16 + 0.3965 * t * v**0.16
    print(int(wci), 'індекс прохолодності вітру')
else:
    wci = 13.12 + 0.6215 * t - 11.37 * v**0.16 + 0.3965 * t * v**0.16 
    print(int(wci), 'дані некоретні')
import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny Yaroslav')   
