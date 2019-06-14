
g = {
    0: 'Dragon',
    1: 'Snake',
    2: 'Horse',
    3: 'Shep',
    4: 'Monkey',
    5: 'Rooster',
    6: 'Dog',
    7: 'Pog',
    8: 'Rat',
    9: 'Oh',
    10: 'Tiger',
    11: 'Hare',
}
print(g[(int(input('>>> Рік = ')) - 2000) % 12])
import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)
printTimeStamp('Негоденко and Нескоромний Я.Д.')


