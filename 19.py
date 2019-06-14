a = input('Відпустка чи вихідний або будень ')
if a == 'відпустка' or a == 'вихідний':
    print('Не включать будільнік')
else:
    print('включить будільнік')
import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny Yaroslav')    
          
