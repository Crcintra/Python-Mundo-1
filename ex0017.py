import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do catedo adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))