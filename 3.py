a = input("Введіть букву: ")
if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
    print('Голосна')
elif a == "y":
    print('Голосна або приголосна')
else:
    print('приголосна')
import datetime    
def printTimeStamp(name):

  print('Автор програми:Негоденко ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny Yaroslav')    
          
