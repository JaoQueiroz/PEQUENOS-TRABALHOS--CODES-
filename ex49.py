# MOSTRAR TABUADA DE NÚMERO ESCOLHIDO ----------------EX 49
num = int(input('DIGITE UM NÚMERO PARA VER SUA TABUADA: '))
for c in range(1, 11):
	print('{} X {:2} = {}'.format(num, c, num*c))
