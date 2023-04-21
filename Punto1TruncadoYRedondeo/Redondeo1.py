import math

var1 = 13/14

var2 = 6/7

var3 = 2 * math.e

redondeo1 = round(var1, 3)
redondeo2 = round(var2, 3)
redondeo3 = round(var3, 3)


print('13/14 redondeo: {}'.format(redondeo1))
print('6/7 redondeo: {}'.format(redondeo2))
print('2e redondeo: {}'.format(redondeo3))

resta = round(redondeo1 - redondeo2, ndigits=3)
division = round(resta/redondeo3, 3)

print('13/14 - 6/7 redondeo: {}'.format(resta))
print('(13/14 - 6/7)/2e redondeo: {}'.format(division))
print('Error absoluto: {}'.format(abs(division - (var1-var2)/var3)))
print('Error relativo: {}'.format((abs(division - (var1-var2)/var3))/((var1-var2)/var3)))