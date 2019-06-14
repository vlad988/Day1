a = int(input('Введіть 13-цифровий міжнародний стандартний номер книги: '))
s = str(a)
d1 = int(s[0])

d2 = int(s[1])

d3 = int(s[2])

d4 = int(s[3])

d5 = int(s[4])

d6 = int(s[5])

d7 = int(s[6])

d8 = int(s[7])

d9 = int(s[8])

d10 = int(s[9])

d11 = int(s[10])

d12 =  int(s[11])

d13 = int(s[12])


lol = (d1 * 1)+(d2 * 3)+(d3*1)+(d4*3)+(d5*1)+(d6*3)+(d7*1)+(d8*3)+(d9*1)+(d10*3)+(d11*1)+(d12*3)+(d13*1)
joke = 10 -(lol%10)
if joke == d13:
    print('Валідність пітверджена')
    print(joke)
else:
    print('Валідність непітверджено')
import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny Yaroslav')    
          

