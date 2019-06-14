d = float(input("кількість днів "))
h = float(input("кількість годин "))
m = float(input("кільсть хвилин "))
s = float(input("кількість секунд "))
q = (d*24)*60*60
w = h*60*60
m = m*60
sec = q+w+m+s
print(sec,'секунди')

import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny Yaroslav')    
          
