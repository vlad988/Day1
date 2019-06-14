a = int(input('Цельсія '))
F = int(a * 9/5 + 32)
K = int(a + 273.15)
print(a, 'Celsia')
print(F, 'Farengeyt')
print(K, 'Kelvin')
import datetime

def printTimeStamp(name):

  print('Автор програми:Негоденко ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny')
