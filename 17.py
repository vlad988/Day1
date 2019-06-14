import math
s = float(input('Довжина сторони '))
n = float(input('Кількість сторін '))
S = (n*s**2)/(4*math.tan(math.pi/n))
print(S)
import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny Yaroslav')
