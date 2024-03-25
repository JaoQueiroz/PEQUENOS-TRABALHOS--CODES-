#LER 2 VALORES E COM MENU DE OPERAÇÕES----------------------------EX 59
from time import sleep
print('ESTE MÓDULO CONVERTE O VALOR QUE VOCÊ TEM NA CARTEIRA EM REAIS (R$) PARA UM VALOR EM DÓLARES')
print('-=-=-' * 21)
sleep(1)
print('QUANTO EM DINHEIRO R$ (REAIS) VOCÊ TEM NA CARTEIRA? ')
n1 = float(input('POR FAVOR, USE PONTO (.) COMO SEPARADOR DOS CENTAVOS, CASO PRECISE - R$ '))
n1_limitado = round(n1, 2)
print('-=-=-' * 21)
sleep(1)
print('EM RELAÇÃO Á NOSSA MOEDA R$ (REAL), QUANTO ESTÁ VALENDO O DÓLAR (US$) NESTE MOMENTO? ')
print('(FAÇA UMA BREVE PESQUISA CASO PRECISE) ')
print('-=-=-' * 21)
sleep(1)
print('COTAÇÃO DÓLAR (US$) ATUAL ')
n2 = float(input('POR FAVOR, USE PONTO (.) COMO SEPARADOR DOS CENTAVOS, CASO PRECISE - R$ '))
n2_limitado = round(n2, 2)
opção = 0
while opção != 3:
	print('''     [ 1 ] CONVERTER SEU VALOR EM REAIS (R$) PARA DÓLARES (US$):
     [ 2 ] INFORMAR NOVOS VALORES... RECOMEÇAR SEU CÁLCULO:
     [ 3 ] SAIR DO PROGRAMA''')
	opção = int(input('>>>>>>QUAL É A SUA OPÇÃO? '))
	if opção == 1:
		produto = n1 / n2
		print('TENDO R${} NA CARTEIRA, COM O DÓLAR VALENDO R${} REAIS, VOCÊ TERIA O EQUIVALENTE A US$ {:.2f} DÓLARES'.format(n1_limitado, n2_limitado, produto))
	elif opção == 2:
		print('INFORME OS NÚMEROS NOVAMENTE:')
		print('QUANTO EM DINHEIRO R$ (REAIS) VOCÊ TEM NA CARTEIRA? ')
		n1 = float(input('POR FAVOR, USE PONTO (.) COMO SEPARADOR DOS CENTAVOS, CASO PRECISE - R$ '))
		n1_limitado = round(n1, 2)
		print('COTAÇÃO DÓLAR (US$) ATUAL ')
		n2 = float(input('POR FAVOR, USE PONTO (.) COMO SEPARADOR DOS CENTAVOS, CASO PRECISE - R$ '))
		n2_limitado = round(n2, 2)
		produto = n1 / n2
		print('TENDO R${} NA CARTEIRA, COM O DÓLAR VALENDO R${} REAIS, VOCÊ TERIA O EQUIVALENTE A US$ {:.2f} DÓLARES'.format(n1_limitado, n2_limitado, produto))
	elif opção == 3:
		print('FINALIZANDO...')
	else:
		print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE')
	print('-=-=-' * 21)
	sleep(1)
print('FIM DO PROGRAMA! VOLTE SEMPRE!')
print('-=-=-' * 21)
sleep(3)