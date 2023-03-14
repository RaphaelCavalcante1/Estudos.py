from math import sin, cos, tan, radians
ang = float(input('Digite o angulo:'))
g = sin(radians(ang))
h = cos(radians(ang))
j = tan(radians(ang))
print('O ângulo de {} equivale a {:.2f} SENO \nO ângulo de {} equivale a {:.2f} COSSENO'.format(ang, g, ang, h))
print('O ângulo de {} equivale a {:.2f} TANGENTE'.format(ang, j))

