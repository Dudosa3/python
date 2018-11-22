from random import randrange
hod = randrange(3)

if hod == 0:
	tah_pocitace = 'nuzky'
if hod == 1:
	tah_pocitace = 'kamen'
if hod == 2:
	tah_pocitace = 'papir'
	
tah_cloveka = input('kamen, nuzky, nebo papir? ')

if tah_cloveka == 'kamen':
    if tah_pocitace == 'kamen':
        print('Plichta.')
    elif tah_pocitace == 'nuzky':
        print('Vyhrala jsi!')
    elif tah_pocitace == 'papir':
        print('Počitač vyhral.')
elif tah_cloveka == 'nuzky':
    if tah_pocitace == 'kamen':
        print('Počitač vyhral.')
    elif tah_pocitace == 'nuzky':
        print('Plichta.')
    elif tah_pocitace == 'papir':
        print('Vyhrala jsi!')
elif tah_cloveka == 'papir':
    if tah_pocitace == 'kamen':
        print('Vyhrala jsi!')
    elif tah_pocitace == 'nuzky':
        print('Počitač vyhral.')
    elif tah_pocitace == 'papir':
        print('Plichta.')
else:
    print('Nerozumim.')
print("To byl" ,tah_pocitace,"!!!!")