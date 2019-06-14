import math
t1 = float(input('Ввести широту '))
g1 = float(input('Ввести довготу '))
t2 = float(input('Ввести широту другой координати '))
g2 = float(input('Ввести довготу другой координати '))
road = 6371.01 * math.acos(math.sin(math.radians(t1)) * math.sin(math.radians(t2)) + math.cos(math.radians(t1)) * math.cos(math.radians(t2)) * math.cos(math.radians(g1 - g2)))
print(road,'km')
import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny Yaroslav')
