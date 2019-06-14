import datetime
a = float(input("Введіть роки вашого життя: "))
def Dog():
    if a < 1:
        print("Неправильно введене число")
        return;
    else:
        print("Приймаю інформацію")
        a1 = 2
        a2 = a - 2
        b1 = a1 / 10.5
        b2 = a1 / 4
        b3 = a2 / 7
        b4 = b2 + b3
        b5 = b1 + b3
        print("У собачих роках ваше життя було: ",+ b4)
        print("У собачих роках ваше життя було: ",+ b5)
        
import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
Dog()


printTimeStamp("Nehodenko and Neskoromny Y.D.")
