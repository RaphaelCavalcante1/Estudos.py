n = input('digite algo:')
print('qual é o tipo primitivo dessa palavra?', type(n))
print('É alfabetico?', n.isalpha())
print('É algo numerico?', n.isnumeric())
print('Esta em letra maiuscula?', n.isupper())
print('Esta em letra minuscula?', n.islower())
print('É algo alfanumerico?', n. isalnum())
print('esta capitalizada?', n.istitle())