a = int(input('Введіть ціле число '))
suma =(a*(a+1))/2
print(suma)
import datetime

def printTimeStamp(name):

  print('Автор програми:Негоденко ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny')
