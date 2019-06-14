ball = input('Введіть буквенну оцінку(від A до F): ')

if ball == 'A+' :
	print('Оцінка більше 4 балів')
elif ball == 'A' :
	print('Ваша оцінка становить: 4.0 бала')
elif ball == 'A-' :
	print('Ваша оцінка становить: 3.7 бала')
elif ball == 'B+' :
	print('Ваша оцінка становить: 3.3 бала')
elif ball == 'B' :
	print('Ваша оцінка становить: 3.0 бала')
elif ball == 'B-' :
	print('Ваша оцінка становить: 2.7 бала')
elif ball == 'C+' :
	print('Ваша оцінка становить: 2.3 бала')
elif ball == 'C' :
	print('Ваша оцінка становить: 2.0 бала')
elif ball == 'C-' :
	print('Ваша оцінка становить: 1.7 бала')
elif ball == 'D+' :
	print('Ваша оцінка становить: 1.3 бала')
elif ball == 'D' :
	print('Ваша оцінка становить: 1.0 бал')
elif ball == 'F' :
	print('Ваша оцінка становить: 0 балов')
else:
	print('Помилка, введіть буквенну оцінку від A до F')

import datetime
def printTimeStamp(name):									  
 print('Автор програми: ' + name)							  
 print('Час компіляції: ' + str(datetime.datetime.now()))
print(printTimeStamp('Негоденко і Нескоромний'))
