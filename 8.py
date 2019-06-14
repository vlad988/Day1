a = float(input('штучки: '))
b = float(input('штукенції: '))
c = (a*75)+(b*112)
print(a,'штучки', b,'штукенції','\n','Обща маса в грамах:', c)

import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny Yaroslav')    
          

