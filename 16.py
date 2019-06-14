import math
a = float(input('radius '))
S = math.pi*a**2
v = 4/3*math.pi*a**3
print(a, 'radius')
print(S, 'площа')
print(v, 'обєм')
import datetime

def printTimeStamp(name):

  print('Автор програми:Негоденко ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny')
