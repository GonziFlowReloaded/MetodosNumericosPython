import math

def truncate(number: float, max_decimals: int) -> float:
    int_part, dec_part = str(number).split(".")
    return float(".".join((int_part, dec_part[:max_decimals])))


var1 = 13/14

var2 = 6/7

var3 = 2 * math.e

truncado1 = truncate(float(var1), 3)
truncado2 = truncate(float(var2), 3)
truncado3 = truncate(float(var3), 3)


print('13/14 Truncado: {}'.format(truncado1))
print('6/7 Truncado: {}'.format(truncado2))
print('2e Truncado: {}'.format(truncado3))

resta = truncate(truncado1 - truncado2, 3)
division = truncate(resta/truncado3, 3)
print('13/14 - 6/7 Truncado: {}'.format(resta))
print('(13/14 - 6/7)/2e Truncado: {}'.format(division))
print('Error absoluto: {}'.format(abs(division - (var1-var2)/var3)))
print('Error relativo: {}'.format((abs(division - (var1-var2)/var3))/((var1-var2)/var3)))