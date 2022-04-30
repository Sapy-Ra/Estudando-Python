#Exercicio 10 - Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).
#Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

NOME = input('')
SALARY_FIX = float(input(''))
TOTAL_SELL = float(input(''))

BONUS = float(TOTAL_SELL * (15/100))

TOTAL = SALARY_FIX + BONUS

print('TOTAL = R$ {:.2f}'.format(TOTAL))