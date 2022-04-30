#Exercicio 11 - Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

ITEM_1 = input().split(' ')
ITEM_2 = input().split(' ')

COD1, QTDE1, VALOR1 = ITEM_1
COD2, QTDE2, VALOR2 = ITEM_2


SOMA = (int(QTDE1) * float(VALOR1)) + (int(QTDE2) * float(VALOR2))

print('VALOR A PAGAR: R$ {:.2f}' .format(SOMA))