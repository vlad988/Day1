a = int(input("Введіть 4 значне число "))

s1 = a%10
a = a//10
s2 = a%10
a = a//10
s3 = a%10
a = a//10
s4 = a%10
a = a//10
print('suma:', s1+s2+s3+s4)
import datetime

def printTimeStamp(name):

  print('Автор програми:Негоденко ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny')

