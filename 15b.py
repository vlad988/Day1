year = int(input("Введіть рік "))
if year % 4 != 0:
    print("Невисокосний")
elif year % 100 == 0:
    if year % 400 == 0:
        print("Високосний")
    else:
        print("Невисокосний")
else:
    print("Високосний")
    
import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny Yaroslav') 
