import math
t1 = float(49.8382600) 
g1 = float(24.0232400) ##Координати Львова
t2 = float(46.4774700)
g2 = float(30.7326200) ##Координати Одеси
t3 = float(49.9808100)
g3 = float(36.2527200) ##Координати Харькова

road1 = 6371.01 * math.acos(math.sin(math.radians(t1)) * math.sin(math.radians(t2)) + math.cos(math.radians(t1)) * math.cos(math.radians(t2)) * math.cos(math.radians(g1 - g2)))
road2 = 6371.01 * math.acos(math.sin(math.radians(t1)) * math.sin(math.radians(t3)) + math.cos(math.radians(t3)) * math.cos(math.radians(t3)) * math.cos(math.radians(g1 - g3)))
road3 = 6371.01 * math.acos(math.sin(math.radians(t2)) * math.sin(math.radians(t3)) + math.cos(math.radians(t2)) * math.cos(math.radians(t3)) * math.cos(math.radians(g2 - g3)))

p = (road1 + road2 +road3)/2
r = p*(p - road1)*(p - road2)*(p - road3)
q = math.sqrt(r)
print(q)

import datetime    
def printTimeStamp(name):

  print('Автор програми:' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Nehodenko and Neskoromny Yaroslav')

