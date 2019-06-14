flag = input("Вчом вимірювать? (Дюйм, метр): ")
if flag == 'Дюйм':
    d = float(input("Зріст: "))
    v = float(input("Маса: "))
    res = 700*(v/d**2)
    print(res)
elif flag == 'метр':
    d = float(input("Зріст: "))
    v = float(input("Маса: "))
    result = (v/d**2)
    print(result)




import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny Yaroslav')    
